"""Tests de la configuration d'administration de l'application contact."""
from django.contrib import admin
from django.test import TestCase

from apps.contact.admin import ContactMessageAdmin
from apps.contact.models import ContactMessage


class ContactMessageAdminTests(TestCase):
    """Vérifie l'enregistrement et la configuration de ContactMessageAdmin."""

    def test_contact_message_is_registered(self):
        self.assertIn(ContactMessage, admin.site._registry)

    def test_admin_configuration(self):
        model_admin = admin.site._registry[ContactMessage]
        self.assertIsInstance(model_admin, ContactMessageAdmin)
        self.assertIn("email", model_admin.list_display)
        self.assertIn("status", model_admin.list_filter)
        self.assertIn("subject", model_admin.search_fields)
        self.assertIn("message", model_admin.readonly_fields)

    def test_add_permission_is_disabled(self):
        model_admin = admin.site._registry[ContactMessage]
        self.assertFalse(model_admin.has_add_permission(request=None))
