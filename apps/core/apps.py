"""Configuration de l'application core."""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """Pages transverses du site : accueil, à propos, pages légales."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.core"
    label = "core"
    verbose_name = "Cœur du site"
