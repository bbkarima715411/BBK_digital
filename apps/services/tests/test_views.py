"""Tests de la vue liste de l'application services."""
from django.test import TestCase
from django.urls import reverse

from apps.services.models import Service


class ServiceListViewTests(TestCase):
    """Tests de la page publique des services."""

    def test_status_and_template(self):
        response = self.client.get(reverse("services:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "services/service_list.html")

    def test_main_heading_present(self):
        response = self.client.get(reverse("services:list"))
        self.assertContains(response, "<h1")
        self.assertContains(response, "Services")

    def test_only_active_services_displayed(self):
        Service.objects.create(
            title="Service actif",
            slug="service-actif",
            short_description="Visible.",
            description="Description.",
        )
        Service.objects.create(
            title="Service inactif",
            slug="service-inactif",
            short_description="Masqué.",
            description="Description.",
            is_active=False,
        )
        response = self.client.get(reverse("services:list"))
        self.assertContains(response, "Service actif")
        self.assertNotContains(response, "Service inactif")

    def test_services_ordered_by_display_order(self):
        second = Service.objects.create(
            title="B", slug="b", short_description="B.", description="B.",
            display_order=2,
        )
        first = Service.objects.create(
            title="A", slug="a", short_description="A.", description="A.",
            display_order=1,
        )
        response = self.client.get(reverse("services:list"))
        self.assertEqual(list(response.context["services"]), [first, second])

    def test_empty_state(self):
        response = self.client.get(reverse("services:list"))
        self.assertContains(response, "sera publié très prochainement")
