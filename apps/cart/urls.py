from django.urls import path

from apps.cart import views_http

urlpatterns = [
    path("cart/", views_http.cart_view_http, name="cart"),

    path("card/add/", views_http.add_to_cart_view_http, name="cart_add"),
    path("card/decrease/", views_http.decrease_cart_view_http, name="cart_update"),
    path("card/remove/", views_http.remove_from_cart_view_http, name="cart_remove"),
]

