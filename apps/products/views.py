"""Vues de l'application products."""
from django.views.generic import TemplateView


class ProductListView(TemplateView):
    """Liste des produits numériques BBK Digital.

    Deviendra une ListView branchée sur le modèle Product à l'étape 4.
    """

    template_name = "pages/products.html"
