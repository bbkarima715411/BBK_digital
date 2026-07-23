"""Tests du modèle Service."""
from django.db import IntegrityError
from django.test import TestCase

from apps.services.models import Service


class ServiceModelTests(TestCase):
    """Tests de création, valeurs par défaut et contraintes du modèle Service."""

    def _create_service(self, **kwargs):
        defaults = {
            "title": "Création de sites",
            "slug": "creation-de-sites",
            "short_description": "Sites web professionnels sur mesure.",
            "description": "Description complète du service.",
        }
        defaults.update(kwargs)
        return Service.objects.create(**defaults)

    def test_create_service(self):
        service = self._create_service()
        self.assertIsNotNone(service.pk)
        self.assertIsNotNone(service.created_at)
        self.assertIsNotNone(service.updated_at)

    def test_str_returns_title(self):
        service = self._create_service()
        self.assertEqual(str(service), "Création de sites")

    def test_default_values(self):
        service = self._create_service()
        self.assertTrue(service.is_active)
        self.assertEqual(service.display_order, 0)
        self.assertEqual(service.icon, "")

    def test_slug_is_unique(self):
        self._create_service()
        with self.assertRaises(IntegrityError):
            self._create_service(title="Autre service")

    def test_default_ordering(self):
        second = self._create_service(slug="service-b", title="B", display_order=2)
        first = self._create_service(slug="service-a", title="A", display_order=1)
        self.assertEqual(list(Service.objects.all()), [first, second])
