from django.urls import reverse
from rest_framework.test import APITestCase

from apps.cart.models import CartItem
from apps.catalog.models import Product


class CartApiTest(APITestCase):

    def setUp(self):
        self.product = Product.objects.create(
            title="API Brake Test",
            price=100,
            stock=10,
        )

    def test_add_product_to_cart_api(self):
        url = reverse("cart:api_cart_add")

        response = self.client.post(
            url,
            {"product_id": self.product.id},
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        self.assertEqual(CartItem.objects.count(), 1)

        item = CartItem.objects.first()
        self.assertEqual(item.product, self.product)
        self.assertEqual(item.quantity, 1)


    def test_decrease_product_quantity_api(self):
        add_url = reverse("cart:api_cart_add")
        decrease_url = reverse("cart:api_cart_decrease")

        # add twice
        self.client.post(add_url, {"product_id": self.product.id}, format="json")
        self.client.post(add_url, {"product_id": self.product.id}, format="json")

        response = self.client.post(
            decrease_url,
            {"product_id": self.product.id},
            format="json"
        )

        self.assertEqual(response.status_code, 200)

        item = CartItem.objects.first()
        self.assertEqual(item.quantity, 1)

    def test_get_cart_api(self):
        add_url = reverse("cart:api_cart_add")
        cart_url = reverse("cart:api_cart")

        self.client.post(add_url, {"product_id": self.product.id}, format="json")

        response = self.client.get(cart_url)

        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertTrue(len(data.get("items", [])) >= 1)

