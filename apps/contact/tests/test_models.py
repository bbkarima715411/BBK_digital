"""Tests du modèle ContactMessage."""
from django.core.exceptions import ValidationError
from django.test import TestCase

from apps.contact.models import ContactMessage


def create_message(**kwargs):
    defaults = {
        "name": "Jean Dupont",
        "email": "jean.dupont@example.com",
        "subject": "Demande de devis",
        "message": "Bonjour, je souhaite un devis pour un site vitrine.",
    }
    defaults.update(kwargs)
    return ContactMessage.objects.create(**defaults)


class ContactMessageModelTests(TestCase):
    """Tests de création, valeurs par défaut et validation de ContactMessage."""

    def test_create_message(self):
        message = create_message()
        self.assertIsNotNone(message.pk)
        self.assertIsNotNone(message.created_at)

    def test_str_contains_name_and_subject(self):
        message = create_message()
        self.assertEqual(str(message), "Jean Dupont — Demande de devis")

    def test_default_values(self):
        message = create_message()
        self.assertEqual(message.status, ContactMessage.Status.NEW)
        self.assertFalse(message.is_read)
        self.assertEqual(message.company, "")

    def test_status_choices(self):
        expected = {"new", "in_progress", "answered", "archived", "spam"}
        self.assertEqual(set(ContactMessage.Status.values), expected)

    def test_invalid_email_raises_validation_error(self):
        message = ContactMessage(
            name="Jean Dupont",
            email="adresse-invalide",
            subject="Sujet",
            message="Message.",
        )
        with self.assertRaises(ValidationError):
            message.full_clean()

    def test_default_ordering_most_recent_first(self):
        first = create_message(subject="Premier")
        second = create_message(subject="Second")
        self.assertEqual(list(ContactMessage.objects.all()), [second, first])
