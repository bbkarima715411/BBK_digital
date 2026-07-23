"""Administration de l'application products."""
from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Administration des produits numériques BBK Digital."""

    list_display = (
        "name",
        "product_type",
        "status",
        "is_featured",
        "is_published",
        "display_order",
    )
    list_filter = ("is_published", "is_featured", "status", "product_type")
    search_fields = ("name", "short_description", "description")
    ordering = ("display_order", "name")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created_at", "updated_at")
    list_editable = ("is_featured", "is_published", "display_order")
    actions = ("publish_products", "unpublish_products", "archive_products")

    @admin.action(description="Publier les produits sélectionnés")
    def publish_products(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description="Dépublier les produits sélectionnés")
    def unpublish_products(self, request, queryset):
        queryset.update(is_published=False)

    @admin.action(description="Archiver les produits sélectionnés")
    def archive_products(self, request, queryset):
        queryset.update(status=Product.Status.ARCHIVED, is_published=False)
