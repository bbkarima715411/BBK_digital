"""Configuration de l'application services."""
from django.apps import AppConfig


class ServicesConfig(AppConfig):
    """Catalogue des services proposés par BBK Digital."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.services"
    label = "services"
    verbose_name = "Services"
