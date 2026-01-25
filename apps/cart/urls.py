from django.urls import path

from apps.cart import views

urlpatterns = [
    path("cart/", views.cart_view_http, name="cart"),

]