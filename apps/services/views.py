"""Vues de l'application services."""
from django.views.generic import TemplateView


class ServiceListView(TemplateView):
    """Liste des services proposés par le studio.

    Deviendra une ListView branchée sur le modèle Service à l'étape 4.
    """

    template_name = "pages/services.html"
