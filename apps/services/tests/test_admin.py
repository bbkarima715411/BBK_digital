"""Tests de la configuration d'administration de l'application services."""
from django.contrib import admin
from django.test import TestCase

from apps.services.admin import ServiceAdmin
from apps.services.models import Service


class ServiceAdminTests(TestCase):
    """Vérifie l'enregistrement et la configuration de ServiceAdmin."""

    def test_service_is_registered(self):
        self.assertIn(Service, admin.site._registry)

    def test_admin_configuration(self):
        model_admin = admin.site._registry[Service]
        self.assertIsInstance(model_admin, ServiceAdmin)
        self.assertIn("title", model_admin.list_display)
        self.assertIn("is_active", model_admin.list_filter)
        self.assertIn("title", model_admin.search_fields)
        self.assertEqual(model_admin.prepopulated_fields, {"slug": ("title",)})
        self.assertIn("created_at", model_admin.readonly_fields)
