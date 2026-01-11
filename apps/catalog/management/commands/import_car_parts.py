
from django.core.management.base import BaseCommand
from apps.catalog.models import Product, Tag, ProductTag
from faker import Faker
import cloudinary.api
import random


fake = Faker()

class Command(BaseCommand):
    help = "Import car parts from Cloudinary"

    def handle(self, *args, **options):
        result = cloudinary.api.resources(
            resource_type="image",
            type="upload",
            max_results=22,
        )

        for item in result["resources"]:

            asset_folder = item.get("asset_folder")
            image_url = item.get("secure_url")

            # error protection  'asset_folder' should be 'car_parts/compressor/img1'
            if not asset_folder:
                continue
            if not image_url:
                continue
            if not asset_folder.startswith("car_parts/"):
                continue
            parts = asset_folder.split("/")
            if len(parts) < 2:
                continue
            part_name = parts[1].strip()
            if not part_name:
                continue


            #If not, we create a tag and get its ID.
            tag, created = Tag.objects.get_or_create(name=part_name)
            tag_id = tag.id

            #We make a record in the product table and get the record ID.
            product = Product.objects.create(
                title = f"{part_name.replace('_', ' ').title()} {fake.word().capitalize()}",
                description="\n\n".join(
                    " ".join(fake.words(nb=50)) for _ in range(5)
                ),
                price=random.randint(50, 500),
                image_url=image_url,
                stock=random.randint(0, 20),
            )
            product_id = product.id

            #We make a record in the ProductTag table
            ProductTag.objects.get_or_create(product_id=product_id, tag_id=tag_id)
        print("Database data generation is complete")

