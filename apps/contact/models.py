"""Modèles de l'application contact."""
from django.core.validators import EmailValidator
from django.db import models

from apps.core.models import TimeStampedModel


class ContactMessage(TimeStampedModel):
    """Message reçu via le formulaire de contact du site."""

    class Status(models.TextChoices):
        NEW = "new", "Nouveau"
        IN_PROGRESS = "in_progress", "En cours de traitement"
        ANSWERED = "answered", "Répondu"
        ARCHIVED = "archived", "Archivé"
        SPAM = "spam", "Indésirable"

    name = models.CharField("nom", max_length=150)
    email = models.EmailField("adresse e-mail", validators=[EmailValidator()])
    company = models.CharField("entreprise", max_length=150, blank=True)
    subject = models.CharField("sujet", max_length=200)
    message = models.TextField("message")
    status = models.CharField(
        "statut",
        max_length=20,
        choices=Status.choices,
        default=Status.NEW,
    )
    is_read = models.BooleanField("lu", default=False)

    class Meta:
        verbose_name = "message de contact"
        verbose_name_plural = "messages de contact"
        ordering = ["-created_at"]
        indexes = [
            models.Index(fields=["status"]),
            models.Index(fields=["is_read"]),
        ]

    def __str__(self):
        return f"{self.name} — {self.subject}"
