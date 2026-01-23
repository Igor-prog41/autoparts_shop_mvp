from django.core.management.base import BaseCommand
from django.core.management import call_command
from apps.catalog.models import Product

class Command(BaseCommand):
    help = "Seed initial database data if empty"

    def handle(self, *args, **kwargs):
        if Product.objects.exists():
            self.stdout.write(self.style.SUCCESS("Data already exists. Skipping seed."))
            return

        self.stdout.write("Loading initial data...")
        call_command("loaddata", "fixtures/initial_data.json")
        self.stdout.write(self.style.SUCCESS("Initial data loaded."))