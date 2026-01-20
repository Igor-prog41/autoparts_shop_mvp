from django.contrib import admin
from .models import PageVisit


@admin.register(PageVisit)
class PageVisitAdmin(admin.ModelAdmin):
    list_display = ("path", "ip_address", "created_at")
    list_filter = ("path", "created_at")
    search_fields = ("ip_address", "path")

