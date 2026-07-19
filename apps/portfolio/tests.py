"""Tests de l'application portfolio."""
from django.test import TestCase
from django.urls import reverse


class PortfolioUrlsTests(TestCase):
    """Vérifie que les URLs de l'application portfolio sont résolues."""

    def test_list_url_resolves(self):
        self.assertEqual(reverse("portfolio:list"), "/realisations/")
