"""Tests de la configuration d'administration de l'application portfolio."""
from django.contrib import admin
from django.test import TestCase

from apps.portfolio.admin import ProjectAdmin, ProjectCategoryAdmin, TechnologyAdmin
from apps.portfolio.models import Project, ProjectCategory, Technology


class PortfolioAdminTests(TestCase):
    """Vérifie l'enregistrement et la configuration des admins portfolio."""

    def test_models_are_registered(self):
        self.assertIn(Project, admin.site._registry)
        self.assertIn(ProjectCategory, admin.site._registry)
        self.assertIn(Technology, admin.site._registry)

    def test_project_admin_configuration(self):
        model_admin = admin.site._registry[Project]
        self.assertIsInstance(model_admin, ProjectAdmin)
        self.assertIn("title", model_admin.list_display)
        self.assertIn("is_published", model_admin.list_filter)
        self.assertIn("technologies", model_admin.filter_horizontal)
        self.assertEqual(model_admin.prepopulated_fields, {"slug": ("title",)})
        self.assertIn("created_at", model_admin.readonly_fields)

    def test_category_admin_configuration(self):
        model_admin = admin.site._registry[ProjectCategory]
        self.assertIsInstance(model_admin, ProjectCategoryAdmin)
        self.assertEqual(model_admin.prepopulated_fields, {"slug": ("name",)})

    def test_technology_admin_configuration(self):
        model_admin = admin.site._registry[Technology]
        self.assertIsInstance(model_admin, TechnologyAdmin)
        self.assertIn("name", model_admin.search_fields)
