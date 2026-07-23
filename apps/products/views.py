"""Vues de l'application products."""
from django.views.generic import ListView

from .models import Product


class ProductListView(ListView):
    """Liste des produits publiés, dans l'ordre d'affichage défini."""

    model = Product
    template_name = "products/product_list.html"
    context_object_name = "products"

    def get_queryset(self):
        """Seuls les produits publiés sont affichés publiquement."""
        return Product.objects.filter(is_published=True)
