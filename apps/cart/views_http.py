from django.shortcuts import render,redirect, get_object_or_404
from .services import get_cart, get_or_create_cart, add_product_to_cart

from apps.catalog.models import Product




def cart_view_http(request):
    cart = get_cart(request)
    items = cart.items.select_related("product") if cart else []

    total_price = sum(item.quantity * item.product.price for item in items)

    return render(request, "cart/cart.html", {
        "cart": cart,
        "items": items,
        "total_price": total_price
    })


def add_to_cart_view_http(request):
    if request.method != "POST":
        return redirect("catalog")

    product_id = request.POST.get("product_id")
    if not product_id:
        return redirect(request.META.get("HTTP_REFERER", "catalog"))

    product = get_object_or_404(Product, id=product_id)

    cart = get_or_create_cart(request)
    add_product_to_cart(cart, product)

    return redirect(request.META.get("HTTP_REFERER", "catalog"))


def decrease_cart_view_http():
    return None


def remove_from_cart_view_http():
    return None