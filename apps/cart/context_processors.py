from apps.cart.models import Cart,CartItem


def cart_items_count(request):

    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        if not session_id:
            return {"cart_items_count": 0}
        cart = Cart.objects.filter(session_key=session_id).first()

    if not cart:
        return {"cart_items_count": 0}

    return {
        "cart_items_count": cart.items.count()
    }