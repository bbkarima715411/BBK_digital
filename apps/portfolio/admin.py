"""Administration de l'application portfolio."""
from django.contrib import admin

from .models import Project, ProjectCategory, Technology


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    """Administration des catégories de projet."""

    list_display = ("name", "display_order", "is_active")
    list_filter = ("is_active",)
    search_fields = ("name",)
    ordering = ("display_order", "name")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("display_order", "is_active")


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    """Administration des technologies."""

    list_display = ("name", "slug")
    search_fields = ("name",)
    ordering = ("name",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """Administration des réalisations du studio."""

    list_display = (
        "title",
        "category",
        "status",
        "is_featured",
        "is_published",
        "display_order",
        "completion_date",
    )
    list_filter = ("is_published", "is_featured", "status", "category")
    search_fields = ("title", "short_description", "description", "client_name")
    ordering = ("display_order", "-completion_date", "title")
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ("technologies",)
    readonly_fields = ("created_at", "updated_at")
    list_editable = ("is_featured", "is_published", "display_order")
    actions = ("publish_projects", "unpublish_projects")

    @admin.action(description="Publier les projets sélectionnés")
    def publish_projects(self, request, queryset):
        queryset.update(is_published=True)

    @admin.action(description="Dépublier les projets sélectionnés")
    def unpublish_projects(self, request, queryset):
        queryset.update(is_published=False)
