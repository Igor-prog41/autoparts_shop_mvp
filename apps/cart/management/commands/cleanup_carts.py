
from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import timedelta

from apps.cart.models import Cart


class Command(BaseCommand):
    help = "Remove session-based carts older than 3 days"

    def handle(self, *args, **options):
        cutoff_date = timezone.now() - timedelta(days=3)

        expired_carts = Cart.objects.filter(
            user_id__isnull=True,
            updated_at__lt=cutoff_date,
        )

        count = expired_carts.count()
        expired_carts.delete()

        self.stdout.write(
            self.style.SUCCESS(
                f"Deleted {count} expired session carts older than 3 days"
            )
        )

