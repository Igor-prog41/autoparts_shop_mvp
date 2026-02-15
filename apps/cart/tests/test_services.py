from django.test import TestCase

from apps.cart.models import Cart, CartItem
from apps.cart.services import add_product_to_cart
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
        item = add_product_to_cart(self.cart, self.product)

        self.assertIsNotNone(item.id)
        self.assertEqual(item.quantity, 1)

    def test_add_product_increments_quantity_if_exists(self):
        add_product_to_cart(self.cart, self.product)
        item = add_product_to_cart(self.cart, self.product)

        self.assertEqual(item.quantity, 2)

    def test_only_one_cart_item_created(self):
        add_product_to_cart(self.cart, self.product)
        add_product_to_cart(self.cart, self.product)

        self.assertEqual(
            CartItem.objects.filter(
                cart=self.cart,
                product=self.product
            ).count(),
            1
        )