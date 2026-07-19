"""Configuration de l'application products."""
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    """Produits numériques BBK Digital.

    Architecture prévue pour accueillir à terme : applications éducatives,
    applications familiales, SaaS, abonnements et outils numériques.
    """

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.products"
    label = "products"
    verbose_name = "Produits"
