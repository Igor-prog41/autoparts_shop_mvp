
from .models import Cart, CartItem


#user cart contents or session cart contents
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