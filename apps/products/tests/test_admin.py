"""Tests de la configuration d'administration de l'application products."""
from django.contrib import admin
from django.test import TestCase

from apps.products.admin import ProductAdmin
from apps.products.models import Product


class ProductAdminTests(TestCase):
    """Vérifie l'enregistrement et la configuration de ProductAdmin."""

    def test_product_is_registered(self):
        self.assertIn(Product, admin.site._registry)

    def test_admin_configuration(self):
        model_admin = admin.site._registry[Product]
        self.assertIsInstance(model_admin, ProductAdmin)
        self.assertIn("name", model_admin.list_display)
        self.assertIn("product_type", model_admin.list_filter)
        self.assertIn("name", model_admin.search_fields)
        self.assertEqual(model_admin.prepopulated_fields, {"slug": ("name",)})
        self.assertIn("created_at", model_admin.readonly_fields)
