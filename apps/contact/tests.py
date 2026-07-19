"""Tests de l'application contact."""
from django.test import TestCase
from django.urls import reverse


class ContactUrlsTests(TestCase):
    """Vérifie que les URLs de l'application contact sont résolues."""

    def test_form_url_resolves(self):
        self.assertEqual(reverse("contact:form"), "/contact/")
