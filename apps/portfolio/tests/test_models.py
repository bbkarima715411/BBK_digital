"""Tests des modèles de l'application portfolio."""
from django.db import IntegrityError
from django.test import TestCase

from apps.portfolio.models import Project, ProjectCategory, Technology


def create_category(**kwargs):
    defaults = {"name": "Sites web", "slug": "sites-web"}
    defaults.update(kwargs)
    return ProjectCategory.objects.create(**defaults)


def create_technology(**kwargs):
    defaults = {"name": "Django", "slug": "django"}
    defaults.update(kwargs)
    return Technology.objects.create(**defaults)


def create_project(category=None, **kwargs):
    defaults = {
        "title": "Site vitrine BBK",
        "slug": "site-vitrine-bbk",
        "short_description": "Site vitrine haut de gamme.",
        "description": "Description complète du projet.",
        "featured_image": "portfolio/sample.jpg",
    }
    defaults.update(kwargs)
    return Project.objects.create(category=category or create_category(), **defaults)


class ProjectCategoryModelTests(TestCase):
    """Tests du modèle ProjectCategory."""

    def test_create_and_str(self):
        category = create_category()
        self.assertIsNotNone(category.pk)
        self.assertEqual(str(category), "Sites web")

    def test_default_values(self):
        category = create_category()
        self.assertTrue(category.is_active)
        self.assertEqual(category.display_order, 0)

    def test_slug_is_unique(self):
        create_category()
        with self.assertRaises(IntegrityError):
            create_category(name="Autres sites")

    def test_default_ordering(self):
        second = create_category(name="B", slug="b", display_order=2)
        first = create_category(name="A", slug="a", display_order=1)
        self.assertEqual(list(ProjectCategory.objects.all()), [first, second])


class TechnologyModelTests(TestCase):
    """Tests du modèle Technology."""

    def test_create_and_str(self):
        technology = create_technology()
        self.assertEqual(str(technology), "Django")

    def test_name_and_slug_are_unique(self):
        create_technology()
        with self.assertRaises(IntegrityError):
            create_technology()

    def test_default_ordering(self):
        postgres = create_technology(name="PostgreSQL", slug="postgresql")
        django = create_technology()
        self.assertEqual(list(Technology.objects.all()), [django, postgres])


class ProjectModelTests(TestCase):
    """Tests du modèle Project et de ses relations."""

    def test_create_and_str(self):
        project = create_project()
        self.assertIsNotNone(project.pk)
        self.assertEqual(str(project), "Site vitrine BBK")

    def test_default_values(self):
        project = create_project()
        self.assertEqual(project.status, Project.Status.COMPLETED)
        self.assertFalse(project.is_featured)
        self.assertFalse(project.is_published)
        self.assertEqual(project.display_order, 0)
        self.assertIsNone(project.completion_date)

    def test_slug_is_unique(self):
        category = create_category()
        create_project(category=category)
        with self.assertRaises(IntegrityError):
            create_project(category=category, title="Autre projet")

    def test_status_choices(self):
        expected = {"in_progress", "completed", "maintenance", "concept"}
        self.assertEqual(set(Project.Status.values), expected)

    def test_category_relation(self):
        category = create_category()
        project = create_project(category=category)
        self.assertEqual(project.category, category)
        self.assertIn(project, category.projects.all())

    def test_technologies_relation(self):
        project = create_project()
        django = create_technology()
        postgres = create_technology(name="PostgreSQL", slug="postgresql")
        project.technologies.add(django, postgres)
        self.assertEqual(project.technologies.count(), 2)
        self.assertIn(project, django.projects.all())

    def test_default_ordering(self):
        category = create_category()
        second = create_project(category=category, slug="b", title="B", display_order=2)
        first = create_project(category=category, slug="a", title="A", display_order=1)
        self.assertEqual(list(Project.objects.all()), [first, second])
