"""Configuration de l'application contact."""
from django.apps import AppConfig


class ContactConfig(AppConfig):
    """Formulaire de contact sécurisé du site BBK Digital."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.contact"
    label = "contact"
    verbose_name = "Contact"
