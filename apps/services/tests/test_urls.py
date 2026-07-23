"""Tests des URLs de l'application services."""
from django.test import TestCase
from django.urls import reverse


class ServicesUrlsTests(TestCase):
    """Vérifie que les URLs de l'application services sont résolues."""

    def test_list_url_resolves(self):
        self.assertEqual(reverse("services:list"), "/services/")
