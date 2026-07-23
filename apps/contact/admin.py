"""Administration de l'application contact."""
from django.contrib import admin

from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """Administration des messages reçus via le formulaire de contact."""

    list_display = ("name", "email", "subject", "status", "is_read", "created_at")
    list_filter = ("status", "is_read")
    search_fields = ("name", "email", "company", "subject", "message")
    ordering = ("-created_at",)
    readonly_fields = (
        "name",
        "email",
        "company",
        "subject",
        "message",
        "created_at",
        "updated_at",
    )
    actions = ("mark_as_read", "mark_as_answered", "mark_as_spam")

    def has_add_permission(self, request):
        """Les messages proviennent uniquement du formulaire public."""
        return False

    @admin.action(description="Marquer comme lus")
    def mark_as_read(self, request, queryset):
        queryset.update(is_read=True)

    @admin.action(description="Marquer comme répondus")
    def mark_as_answered(self, request, queryset):
        queryset.update(status=ContactMessage.Status.ANSWERED, is_read=True)

    @admin.action(description="Marquer comme indésirables")
    def mark_as_spam(self, request, queryset):
        queryset.update(status=ContactMessage.Status.SPAM, is_read=True)
