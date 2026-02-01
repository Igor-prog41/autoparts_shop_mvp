
from django.shortcuts import render, redirect
from .services import create_user
from django.contrib.auth import authenticate, login, logout

from ..cart.models import Cart
from ..cart.services import merge_guest_cart_into_user_cart


def register_view_http(request):
    # receiving session_cart for combining baskets
    session_cart = Cart.objects.filter(session_key=request.session.session_key).first()
    if request.method == "POST":
        try:
            user = create_user(
                request.POST["username"],
                request.POST["email"],
                request.POST["password"]
            )
            login(request, user)
            # combining baskets
            if session_cart:
                merge_guest_cart_into_user_cart(request, session_cart, user)
            return redirect("catalog")

        except Exception as e:
            return render(request, "users/register.html", {"error": str(e)})

    return render(request, "users/register.html")


def login_view_http(request):
    # receiving session_cart for combining baskets
    session_cart = Cart.objects.filter(session_key=request.session.session_key).first()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # combining baskets
            if session_cart:
                merge_guest_cart_into_user_cart(request, session_cart, user)
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

