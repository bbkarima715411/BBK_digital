"""Modèles de l'application portfolio."""
from django.db import models

from apps.core.models import TimeStampedModel


class ProjectCategory(models.Model):
    """Catégorie de réalisation (site web, application, automatisation…)."""

    name = models.CharField("nom", max_length=100)
    slug = models.SlugField("slug", max_length=110, unique=True)
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)
    is_active = models.BooleanField("active", default=True)

    class Meta:
        verbose_name = "catégorie de projet"
        verbose_name_plural = "catégories de projet"
        ordering = ["display_order", "name"]
        indexes = [models.Index(fields=["is_active"])]

    def __str__(self):
        return self.name


class Technology(models.Model):
    """Technologie utilisée dans une réalisation (Django, PostgreSQL…)."""

    name = models.CharField("nom", max_length=100, unique=True)
    slug = models.SlugField("slug", max_length=110, unique=True)

    class Meta:
        verbose_name = "technologie"
        verbose_name_plural = "technologies"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Project(TimeStampedModel):
    """Réalisation du studio BBK Digital."""

    class Status(models.TextChoices):
        IN_PROGRESS = "in_progress", "En cours"
        COMPLETED = "completed", "Terminé"
        MAINTENANCE = "maintenance", "En maintenance"
        CONCEPT = "concept", "Concept"

    title = models.CharField("titre", max_length=200)
    slug = models.SlugField("slug", max_length=210, unique=True)
    short_description = models.CharField("description courte", max_length=255)
    description = models.TextField("description")
    category = models.ForeignKey(
        ProjectCategory,
        verbose_name="catégorie",
        on_delete=models.PROTECT,
        related_name="projects",
    )
    technologies = models.ManyToManyField(
        Technology,
        verbose_name="technologies",
        related_name="projects",
        blank=True,
    )
    featured_image = models.ImageField("image principale", upload_to="portfolio/")
    client_name = models.CharField("nom du client", max_length=150, blank=True)
    project_url = models.URLField("lien du projet", blank=True)
    github_url = models.URLField("lien GitHub", blank=True)
    completion_date = models.DateField("date de réalisation", null=True, blank=True)
    status = models.CharField(
        "statut",
        max_length=20,
        choices=Status.choices,
        default=Status.COMPLETED,
    )
    is_featured = models.BooleanField("mis en avant", default=False)
    is_published = models.BooleanField("publié", default=False)
    display_order = models.PositiveIntegerField("ordre d'affichage", default=0)

    class Meta:
        verbose_name = "projet"
        verbose_name_plural = "projets"
        ordering = ["display_order", "-completion_date", "title"]
        indexes = [
            models.Index(fields=["is_published"]),
            models.Index(fields=["is_featured"]),
            models.Index(fields=["status"]),
        ]

    def __str__(self):
        return self.title
