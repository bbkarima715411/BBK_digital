"""Tests de la vue de l'application contact."""
from django.test import TestCase
from django.urls import reverse


class ContactViewTests(TestCase):
    """Tests de la page de contact (structure visuelle, étape 5)."""

    def test_status_and_template(self):
        response = self.client.get(reverse("contact:form"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact/contact.html")

    def test_main_heading_present(self):
        response = self.client.get(reverse("contact:form"))
        self.assertContains(response, "<h1")
        self.assertContains(response, "Contact")

    def test_form_structure_present(self):
        response = self.client.get(reverse("contact:form"))
        self.assertContains(response, "<form")
        self.assertContains(response, "csrfmiddlewaretoken")
        for field in ("name", "email", "company", "subject", "message"):
            self.assertContains(response, f'name="{field}"')

    def test_contact_email_present(self):
        response = self.client.get(reverse("contact:form"))
        self.assertContains(response, "bbk.digital.contact@gmail.com")
