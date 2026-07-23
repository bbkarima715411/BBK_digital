"""Tests de la vue liste de l'application portfolio."""
from django.test import TestCase
from django.urls import reverse

from apps.portfolio.models import Project, ProjectCategory


def create_project(**kwargs):
    category = kwargs.pop(
        "category", None
    ) or ProjectCategory.objects.get_or_create(name="Sites", slug="sites")[0]
    defaults = {
        "title": "Projet publié",
        "slug": "projet-publie",
        "short_description": "Description courte.",
        "description": "Description.",
        "featured_image": "portfolio/sample.jpg",
        "is_published": True,
    }
    defaults.update(kwargs)
    return Project.objects.create(category=category, **defaults)


class ProjectListViewTests(TestCase):
    """Tests de la page publique des réalisations."""

    def test_status_and_template(self):
        response = self.client.get(reverse("portfolio:list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "portfolio/project_list.html")

    def test_main_heading_present(self):
        response = self.client.get(reverse("portfolio:list"))
        self.assertContains(response, "<h1")
        self.assertContains(response, "Réalisations")

    def test_only_published_projects_displayed(self):
        create_project()
        create_project(
            title="Projet brouillon", slug="projet-brouillon", is_published=False
        )
        response = self.client.get(reverse("portfolio:list"))
        self.assertContains(response, "Projet publié")
        self.assertNotContains(response, "Projet brouillon")

    def test_projects_ordered_by_display_order(self):
        second = create_project(title="B", slug="b", display_order=2)
        first = create_project(title="A", slug="a", display_order=1)
        response = self.client.get(reverse("portfolio:list"))
        self.assertEqual(list(response.context["projects"]), [first, second])

    def test_empty_state(self):
        response = self.client.get(reverse("portfolio:list"))
        self.assertContains(response, "seront publiées ici")
