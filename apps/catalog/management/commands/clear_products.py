
from django.core.management.base import BaseCommand
from django.db import connection

from apps.catalog.models import Product, Tag, ProductTag


class Command(BaseCommand):
    help = "Delete products, tags and relations and reset IDs (SQLite only)"

    def handle(self, *args, **options):
        product_count = Product.objects.count()
        tag_count = Tag.objects.count()
        relation_count = ProductTag.objects.count()

        with connection.cursor() as cursor:
            # 1. Relations (through table)
            cursor.execute("DELETE FROM catalog_producttag;")
            cursor.execute(
                "DELETE FROM sqlite_sequence WHERE name='catalog_producttag';"
            )

            # 2. Products
            cursor.execute("DELETE FROM catalog_product;")
            cursor.execute(
                "DELETE FROM sqlite_sequence WHERE name='catalog_product';"
            )

            # 3. Tags
            cursor.execute("DELETE FROM catalog_tag;")
            cursor.execute(
                "DELETE FROM sqlite_sequence WHERE name='catalog_tag';"
            )

        self.stdout.write(
            self.style.SUCCESS(
                f"Deleted: {product_count} products, "
                f"{tag_count} tags, "
                f"{relation_count} relations. IDs reset."
            )
        )
