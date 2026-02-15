from django.test import TestCase

from apps.cart.models import Cart, CartItem
from apps.cart import services
from apps.catalog.models import Product


class AddProductToCartServiceTest(TestCase):

    def setUp(self):
        self.cart = Cart.objects.create(session_key="test-session")

        self.product = Product.objects.create(
            title="Brake Fluid Test",
            price=15,
            stock=10,
        )

    def test_add_product_creates_cart_item(self):
        item = services.add_product_to_cart(self.cart, self.product)

        self.assertIsNotNone(item.id)
        self.assertEqual(item.quantity, 1)

    def test_add_product_increments_quantity_if_exists(self):
        services.add_product_to_cart(self.cart, self.product)
        item = services.add_product_to_cart(self.cart, self.product)

        self.assertEqual(item.quantity, 2)

    def test_only_one_cart_item_created(self):
        services.add_product_to_cart(self.cart, self.product)
        services.add_product_to_cart(self.cart, self.product)

        self.assertEqual(
            CartItem.objects.filter(
                cart=self.cart,
                product=self.product
            ).count(),
            1
        )


class DecreaseProductInCartServiceTest(TestCase):

    def setUp(self):
        self.cart = Cart.objects.create(session_key="test-session")

        self.product = Product.objects.create(
            title="Coolant Test",
            price=25,
            stock=10,
        )

    # --- Item does not exist ---
    def test_decrease_when_item_not_exists_returns_none(self):
        result = services.decrease_product_in_cart(self.cart, self.product)
        self.assertIsNone(result)

    # --- Quantity > 1 ---
    def test_decrease_quantity_when_more_than_one(self):
        item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=3
        )

        result = services.decrease_product_in_cart(self.cart, self.product)

        item.refresh_from_db()

        self.assertIsNotNone(result)
        self.assertEqual(item.quantity, 2)

    # --- Quantity == 1 (delete case) ---
    def test_delete_item_when_quantity_one(self):
        item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=1
        )

        result = services.decrease_product_in_cart(self.cart, self.product)

        self.assertIsNone(result)
        self.assertFalse(
            CartItem.objects.filter(id=item.id).exists()
        )

