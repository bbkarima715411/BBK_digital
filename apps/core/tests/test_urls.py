"""Tests des URLs de l'application core."""
from django.test import TestCase
from django.urls import reverse


class CoreUrlsTests(TestCase):
    """Vérifie que les URLs de l'application core sont résolues."""

    def test_home_url_resolves(self):
        self.assertEqual(reverse("core:home"), "/")

    def test_about_url_resolves(self):
        self.assertEqual(reverse("core:about"), "/a-propos/")

    def test_legal_notice_url_resolves(self):
        self.assertEqual(reverse("core:legal_notice"), "/mentions-legales/")

    def test_privacy_policy_url_resolves(self):
        self.assertEqual(
            reverse("core:privacy_policy"), "/politique-de-confidentialite/"
        )
