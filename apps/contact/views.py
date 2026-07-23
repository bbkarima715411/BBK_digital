"""Vues de l'application contact."""
from django.views.generic import TemplateView


class ContactView(TemplateView):
    """Page de contact.

    Deviendra une FormView (formulaire sécurisé + envoi SMTP) à l'étape 7.
    """

    template_name = "contact/contact.html"
