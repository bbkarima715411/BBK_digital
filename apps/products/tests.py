"""Tests de l'application products."""
from django.test import TestCase
from django.urls import reverse


class ProductsUrlsTests(TestCase):
    """Vérifie que les URLs de l'application products sont résolues."""

    def test_list_url_resolves(self):
        self.assertEqual(reverse("products:list"), "/produits/")
