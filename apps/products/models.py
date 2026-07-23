"""Modèles de l'application products.

Volontairement simple et évolutif : pas d'abonnement, de paiement, de panier,
de licence, de compte utilisateur ni de téléchargement privé à ce stade.
"""
from django.db import models

from apps.core.models import TimeStampedModel


class Product(TimeStampedModel):
    """Produit numérique BBK Digital (application, SaaS, outil…)."""

    class ProductType(models.TextChoices):
        EDUCATIONAL = "educational", "Éducatif"
        FAMILY = "family", "Familial"
        BUSINESS = "business", "Entreprise"
        SAAS = "saas", "SaaS"
        OTHER = "other", "Autre"

    class Status(models.TextChoices):
        CONCEPT = "concept", "Concept"
        IN_DEVELOPMENT = "in_development", "En développement"
        COMING_SOON = "coming_soon", "Bientôt disponible"
        AVAILABLE = "available", "Disponible"
        ARCHIVED = "archived", "Archivé"

    name = models.CharField("nom", max_length=200)
    slug = models.SlugField("slug", max_length=210, unique=True)
    short_description = models.CharField("description courte", max_length=255)
    description = models.TextField("description")
    # Facultative : un produit en phase de concept peut ne pas avoir de visuel.
    featured_image = models.ImageField(
        "image principale", upload_to="products/", blank=True
    )
    product_type = models.CharField(
        "type de produit",
        max_length=20,
        choices=ProductType.choices,
        default=ProductType.OTHER,
    )
    status = models.CharField(
        "statut",
        max_length=20,
        choices=Status.choices,
        default=Status.CONCEPT,
    )
    external_url = models.URLField("lien externe", blank=True)
    is_featured = models.BooleanField("mis en avant", default=False)
    is_published = models.BooleanField("publié", default=False)
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)

    class Meta:
        verbose_name = "produit"
        verbose_name_plural = "produits"
        ordering = ["display_order", "name"]
        indexes = [
            models.Index(fields=["is_published"]),
            models.Index(fields=["is_featured"]),
            models.Index(fields=["status"]),
            models.Index(fields=["product_type"]),
        ]

    def __str__(self):
        return self.name
