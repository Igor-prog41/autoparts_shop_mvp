
from .models import Cart, CartItem


#user cart contents or session cart contents, but we don't create cart if it doesn't exist
def get_cart(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).first()
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        return Cart.objects.filter(session_key=session_id).first()


# creates a user's shopping cart if he is not identified, a session cart
def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart, _ = Cart.objects.get_or_create(user=request.user)
        return cart

    if not request.session.session_key:
        request.session.create()

    cart, _ = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart


# adds a product to the cart or increases by one
def add_product_to_cart(cart, product):
    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={"quantity": 1}
    )

    if not created:
        item.quantity += 1
        item.save()
    return item


# Reduce the number of items in the cart
def decrease_product_in_cart(cart, product):
    item = CartItem.objects.filter(cart=cart, product=product).first()
    if not item:
        return None

    if item.quantity > 1:
        item.quantity -= 1
        item.save(update_fields=["quantity"])
        return item
    else:
        item.delete()
        return None


# removes products from the cart
def remove_product_from_cart(cart, product):
    CartItem.objects.filter(cart=cart, product=product).delete()


#connecting the session cart with the user's cart
def merge_guest_cart_into_user_cart(request, session_cart, user):
    user_cart, _ = Cart.objects.get_or_create(user=user)
    items = session_cart.items.select_related("product")
    for item in items:
        add_product_to_cart(user_cart, item.product)
    session_cart.delete()

