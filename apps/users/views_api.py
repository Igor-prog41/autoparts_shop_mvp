from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import RegisterSerializer

from ..cart.models import Cart
from ..cart.services import merge_guest_cart_into_user_cart


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        # We get the guests' basket by session_key
        session_key = request.session.session_key
        if session_key:
            session_cart = Cart.objects.filter(
                session_key=session_key
            ).first()

            if session_cart:
                merge_guest_cart_into_user_cart(
                    request=request,
                    session_cart=session_cart,
                    user=user
                )

        # We issue JWT
        refresh = RefreshToken.for_user(user)

        return Response({
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                },
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            },
            status=201
        )


class LoginView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        # If login is successful -> tokens are issued
        if response.status_code == 200:
            user = self.user  # SimpleJWT sets it up

            session_key = request.session.session_key
            if session_key:
                session_cart = Cart.objects.filter(
                    session_key=session_key
                ).first()

                if session_cart:
                    merge_guest_cart_into_user_cart(
                        request=request,
                        session_cart=session_cart,
                        user=user
                    )

        return response

class ProfileAPIView(APIView):
    permission_classes = [IsAuthenticated]  # verification JWT

    def get(self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
        })

