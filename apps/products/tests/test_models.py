"""Tests du modèle Product."""
from django.db import IntegrityError
from django.test import TestCase

from apps.products.models import Product


def create_product(**kwargs):
    defaults = {
        "name": "Application éducative BBK",
        "slug": "application-educative-bbk",
        "short_description": "Apprendre en famille.",
        "description": "Description complète du produit.",
    }
    defaults.update(kwargs)
    return Product.objects.create(**defaults)


class ProductModelTests(TestCase):
    """Tests de création, valeurs par défaut et contraintes du modèle Product."""

    def test_create_and_str(self):
        product = create_product()
        self.assertIsNotNone(product.pk)
        self.assertEqual(str(product), "Application éducative BBK")

    def test_default_values(self):
        product = create_product()
        self.assertEqual(product.status, Product.Status.CONCEPT)
        self.assertEqual(product.product_type, Product.ProductType.OTHER)
        self.assertFalse(product.is_featured)
        self.assertFalse(product.is_published)
        self.assertEqual(product.display_order, 0)
        self.assertEqual(product.external_url, "")

    def test_slug_is_unique(self):
        create_product()
        with self.assertRaises(IntegrityError):
            create_product(name="Autre produit")

    def test_product_type_choices(self):
        expected = {"educational", "family", "business", "saas", "other"}
        self.assertEqual(set(Product.ProductType.values), expected)

    def test_status_choices(self):
        expected = {"concept", "in_development", "coming_soon", "available", "archived"}
        self.assertEqual(set(Product.Status.values), expected)

    def test_default_ordering(self):
        second = create_product(name="B", slug="b", display_order=2)
        first = create_product(name="A", slug="a", display_order=1)
        self.assertEqual(list(Product.objects.all()), [first, second])
