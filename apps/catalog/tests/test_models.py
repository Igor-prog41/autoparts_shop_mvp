from django.db import IntegrityError
from django.test import TestCase
from django.templatetags.static import static

from apps.catalog.models import Product, Tag, ProductTag


class ProductModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            title="Brake Pad Premium Ceramic Ultra Long Name For Testing Purpose",
            description=" ".join(["word"] * 50),
            price=99.99,
            stock=5,
            image_url="https://example.com/image.jpg",
        )

    # --- Creation / slug ---
    def test_product_created(self):
        self.assertIsNotNone(self.product.id)

    def test_slug_is_generated(self):
        self.assertIsNotNone(self.product.slug)
        self.assertTrue(len(self.product.slug) > 0)

    def test_slug_is_unique(self):
        p2 = Product.objects.create(
            title=self.product.title,
            price=50,
        )
        self.assertNotEqual(self.product.slug, p2.slug)

    # --- __str__ ---
    def test_str_returns_title(self):
        self.assertEqual(str(self.product), self.product.title)

    # --- short_description ---
    def test_short_description_limits_words(self):
        short_desc = self.product.short_description()
        self.assertTrue(len(short_desc.split()) <= 21)  # 20 words + "…"

    # --- stock_status ---
    def test_stock_status_in_stock(self):
        status = self.product.stock_status
        self.assertEqual(status["text"], "In stock")

    def test_stock_status_out_of_stock(self):
        self.product.stock = 0
        self.product.save()

        status = self.product.stock_status
        self.assertIn("Out of stock", status["text"])

    # --- image_or_placeholder ---
    def test_returns_image_url_if_exists(self):
        self.assertEqual(
            self.product.image_or_placeholder,
            self.product.image_url
        )

    def test_returns_placeholder_if_no_image(self):
        self.product.image_url = ""
        self.product.save()

        self.assertEqual(
            self.product.image_or_placeholder,
            static("part-placeholder.png")
        )


class TagModelTest(TestCase):

    def test_tag_creation(self):
        tag = Tag.objects.create(name="Engine")

        self.assertIsNotNone(tag.id)
        self.assertEqual(tag.name, "Engine")

    def test_tag_name_unique(self):
        Tag.objects.create(name="Brake")

        with self.assertRaises(IntegrityError):
            Tag.objects.create(name="Brake")

    def test_tag_str(self):
        tag = Tag.objects.create(name="Suspension")
        self.assertEqual(str(tag), "Suspension")


class ProductTagModelTest(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            title="Brake Disc Test",
            price=100,
            stock=5,
        )
        self.tag = Tag.objects.create(name="Brake")

    def test_product_tag_creation(self):
        pt = ProductTag.objects.create(
            product=self.product,
            tag=self.tag,
        )

        self.assertIsNotNone(pt.id)
        self.assertEqual(pt.product, self.product)
        self.assertEqual(pt.tag, self.tag)

    def test_product_tag_unique_together(self):
        ProductTag.objects.create(
            product=self.product,
            tag=self.tag,
        )

        with self.assertRaises(IntegrityError):
            ProductTag.objects.create(
                product=self.product,
                tag=self.tag,
            )

    def test_product_tag_str(self):
        pt = ProductTag.objects.create(
            product=self.product,
            tag=self.tag,
        )

        expected = f"{self.product.title} — {self.tag.name}"
        self.assertEqual(str(pt), expected)

    def test_product_tag_deleted_when_product_deleted(self):
        pt = ProductTag.objects.create(
            product=self.product,
            tag=self.tag,
        )

        self.product.delete()

        self.assertFalse(ProductTag.objects.filter(id=pt.id).exists())

    def test_product_tag_deleted_when_tag_deleted(self):
        pt = ProductTag.objects.create(
            product=self.product,
            tag=self.tag,
        )

        self.tag.delete()

        self.assertFalse(ProductTag.objects.filter(id=pt.id).exists())