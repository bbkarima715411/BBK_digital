"""Administration de l'application services."""
from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """Administration des services proposés par le studio."""

    list_display = ("title", "short_description", "display_order", "is_active", "updated_at")
    list_filter = ("is_active",)
    search_fields = ("title", "short_description", "description")
    ordering = ("display_order", "title")
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("created_at", "updated_at")
    list_editable = ("display_order", "is_active")
    actions = ("activate_services", "deactivate_services")

    @admin.action(description="Activer les services sélectionnés")
    def activate_services(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Désactiver les services sélectionnés")
    def deactivate_services(self, request, queryset):
        queryset.update(is_active=False)
