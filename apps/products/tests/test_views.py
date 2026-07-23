"""Tests de la vue liste de l'application products."""
from django.test import TestCase
from django.urls import reverse

from apps.products.models import Product


def create_product(**kwargs):
    defaults = {
        "name": "Produit publié",
        "slug": "produit-publie",
        "short_description": "Description courte.",
        "description": "Description.",
        "is_published": True,
    }
    defaults.update(kwargs)
    return Product.objects.create(**defaults)


class ProductListViewTests(TestCase):
    """Tests de la page publique des produits."""

    def test_status_and_template(self):
        response = self.client.get(reverse("products:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_list.html")

    def test_main_heading_present(self):
        response = self.client.get(reverse("products:list"))
        self.assertContains(response, "<h1")
        self.assertContains(response, "Produits numériques")

    def test_only_published_products_displayed(self):
        create_product()
        create_product(
            name="Produit brouillon", slug="produit-brouillon", is_published=False
        )
        response = self.client.get(reverse("products:list"))
        self.assertContains(response, "Produit publié")
        self.assertNotContains(response, "Produit brouillon")

    def test_products_ordered_by_display_order(self):
        second = create_product(name="B", slug="b", display_order=2)
        first = create_product(name="A", slug="a", display_order=1)
        response = self.client.get(reverse("products:list"))
        self.assertEqual(list(response.context["products"]), [first, second])

    def test_empty_state(self):
        response = self.client.get(reverse("products:list"))
        self.assertContains(response, "en cours de conception")
