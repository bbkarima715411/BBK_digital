"""Configuration de l'application portfolio."""
from django.apps import AppConfig


class PortfolioConfig(AppConfig):
    """Réalisations du studio BBK Digital."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.portfolio"
    label = "portfolio"
    verbose_name = "Portfolio"
