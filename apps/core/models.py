"""Modèles de l'application core : classes de base réutilisables."""
from django.db import models


class TimeStampedModel(models.Model):
    """Modèle abstrait ajoutant les horodatages de création et de mise à jour.

    Hérité par tous les modèles métier du projet pour éviter la duplication.
    """

    created_at = models.DateTimeField("créé le", auto_now_add=True)
    updated_at = models.DateTimeField("mis à jour le", auto_now=True)

    class Meta:
        abstract = True
