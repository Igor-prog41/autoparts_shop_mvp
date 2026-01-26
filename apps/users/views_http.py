from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .services import create_user
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def register_view_http(request):
    if request.method == "POST":
        try:
            user = create_user(
                request.POST["username"],
                request.POST["email"],
                request.POST["password"]
            )
            login(request, user)
            return redirect("catalog")

        except Exception as e:
            return render(request, "users/register.html", {"error": str(e)})

    return render(request, "users/register.html")


def login_view_http(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("catalog")
        else:
            return render(request, "users/login.html",{
                "error": "Incorrect login or password"})

    return render(request, "users/login.html")


def logout_view_http(request):
    logout(request)
    return redirect("catalog")


def profile_view_http(request):
    user = request.user

    context = {
        "user": user
    }

    return render(request, "users/profile.html", context)