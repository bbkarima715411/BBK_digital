"""Vues de l'application portfolio."""
from django.views.generic import TemplateView


class ProjectListView(TemplateView):
    """Liste des réalisations du studio.

    Deviendra une ListView branchée sur le modèle Project à l'étape 4.
    """

    template_name = "pages/portfolio.html"
