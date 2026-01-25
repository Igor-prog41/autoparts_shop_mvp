from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


def login_view_http(request):

    return render(request, 'users/login.html', {

    })

def register_view_http(request):


    return render(request, 'users/register.html', {

    })