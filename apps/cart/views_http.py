from django.shortcuts import render
from .services import get_or_create_cart



def cart_view_http(request):
    cart = get_or_create_cart(request)
    items = cart.items.select_related("product")

    total_price = sum(item.quantity * item.price_snapshot for item in items)

    return render(request, "cart/cart.html", {
        "cart": cart,
        "items": items,
        "total_price": total_price
    })

