"""Modèles de l'application services."""
from django.db import models

from apps.core.models import TimeStampedModel


class Service(TimeStampedModel):
    """Service proposé par le studio BBK Digital."""

    title = models.CharField("titre", max_length=150)
    slug = models.SlugField("slug", max_length=160, unique=True)
    short_description = models.CharField("description courte", max_length=255)
    description = models.TextField("description")
    icon = models.CharField(
        "icône",
        max_length=100,
        blank=True,
        help_text="Nom d'icône ou classe CSS (ex. : icon-web, bi-code-slash).",
    )
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)
    is_active = models.BooleanField("actif", default=True)

    class Meta:
        verbose_name = "service"
        verbose_name_plural = "services"
        ordering = ["display_order", "title"]
        indexes = [
            models.Index(fields=["is_active"]),
            models.Index(fields=["display_order"]),
        ]

    def __str__(self):
        return self.title
