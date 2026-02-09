from django.urls import path

from apps.cart import views_http
from apps.cart import views_api


urlpatterns = [
    path("cart/", views_http.cart_view_http, name="cart"),

    path("card/add/", views_http.add_to_cart_view_http, name="cart_add"),
    path("card/decrease/", views_http.decrease_cart_view_http, name="cart_decrease"),
    path("card/remove/", views_http.remove_product_from_cart_view_http, name="cart_remove"),

    path("api/cart/", views_api.CartRetrieveAPIView.as_view(), name="api_cart"),
    path("api/cart/add/", views_api.AddToCartAPIView.as_view(), name="api_cart_add"),
    path("api/cart/decrease/", views_api.CartDecreaseAPIView.as_view(), name="api_cart_decrease"),
    path("api/cart/remove/", views_api.CartRemoveAPIView.as_view(), name="api_cart_remove"),
]

