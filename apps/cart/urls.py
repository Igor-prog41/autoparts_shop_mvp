from django.urls import path

from apps.cart import views_http

urlpatterns = [
    path("cart/", views_http.cart_view_http, name="cart"),

]