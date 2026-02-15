from django.test import TestCase
from django.db import IntegrityError
from django.contrib.auth import get_user_model

from apps.cart.models import Cart, CartItem
from apps.catalog.models import Product


User = get_user_model()


class CartModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

    def test_cart_created_for_user(self):
        cart = Cart.objects.create(user=self.user)

        self.assertIsNotNone(cart.id)
        self.assertEqual(cart.user, self.user)

    def test_cart_created_with_session_key(self):
        cart = Cart.objects.create(session_key="test-session")

        self.assertEqual(cart.session_key, "test-session")
        self.assertIsNone(cart.user)

    def test_cart_can_exist_without_user_and_session(self):
        cart = Cart.objects.create()

        self.assertIsNotNone(cart.id)

    def test_cart_deleted_when_user_deleted(self):
        cart = Cart.objects.create(user=self.user)

        self.user.delete()

        self.assertFalse(Cart.objects.filter(id=cart.id).exists())


class CartItemModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            title="Oil Filter Test",
            price=20,
            stock=10,
        )

        self.cart = Cart.objects.create(session_key="session123")

    def test_cart_item_created(self):
        item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
            quantity=2
        )

        self.assertIsNotNone(item.id)
        self.assertEqual(item.quantity, 2)

    def test_cart_item_default_quantity(self):
        item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
        )

        self.assertEqual(item.quantity, 1)

    def test_cart_item_unique_cart_product(self):
        CartItem.objects.create(
            cart=self.cart,
            product=self.product,
        )

        with self.assertRaises(IntegrityError):
            CartItem.objects.create(
                cart=self.cart,
                product=self.product,
            )

    def test_cart_item_deleted_when_cart_deleted(self):
        item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
        )

        self.cart.delete()

        self.assertFalse(CartItem.objects.filter(id=item.id).exists())

    def test_cart_item_deleted_when_product_deleted(self):
        item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
        )

        self.product.delete()

        self.assertFalse(CartItem.objects.filter(id=item.id).exists())

    def test_cart_related_name_items(self):
        item = CartItem.objects.create(
            cart=self.cart,
            product=self.product,
        )

        self.assertEqual(self.cart.items.count(), 1)
        self.assertEqual(self.cart.items.first(), item)

