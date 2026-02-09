from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CartSerializer
from apps.cart import services
from ..catalog.models import Product


class CartRetrieveAPIView(APIView):
    def get(self, request):
        cart = services.get_cart(request)
        serializer = CartSerializer(cart)
        return Response(serializer.data)


class AddToCartAPIView(APIView):
    def post(self, request):
        cart = services.get_or_create_cart(request)
        product_id = request.data["product_id"]
        product = get_object_or_404(Product, id=product_id)
        services.add_product_to_cart(cart, product)
        return Response({"status": True})


class CartDecreaseAPIView(APIView):
    def post(self, request):
        cart = services.get_or_create_cart(request)
        product_id = request.data["product_id"]
        product = get_object_or_404(Product, id=product_id)
        services.decrease_product_in_cart(cart, product)
        return Response({"success": True})


class CartRemoveAPIView(APIView):
    def post(self, request):
        cart = services.get_or_create_cart(request)
        product_id = request.data["product_id"]
        product = get_object_or_404(Product, id=product_id)
        services.remove_product_from_cart(cart, product)
        return Response({"success": True})

