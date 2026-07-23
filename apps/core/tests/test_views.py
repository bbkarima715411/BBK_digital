"""Tests des vues de l'application core."""
from django.test import RequestFactory, TestCase
from django.urls import reverse

from apps.core.views import server_error
from apps.portfolio.models import Project, ProjectCategory
from apps.products.models import Product
from apps.services.models import Service


class HomeViewTests(TestCase):
    """Tests de la page d'accueil."""

    def test_status_and_template(self):
        response = self.client.get(reverse("core:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/home.html")
        self.assertTemplateUsed(response, "base.html")

    def test_main_heading_present(self):
        response = self.client.get(reverse("core:home"))
        self.assertContains(
            response, "Des solutions numériques utiles, élégantes et durables"
        )

    def test_navigation_links_present(self):
        response = self.client.get(reverse("core:home"))
        for url_name in (
            "core:home",
            "services:list",
            "portfolio:list",
            "products:list",
            "core:about",
            "contact:form",
        ):
            self.assertContains(response, f'href="{reverse(url_name)}"')

    def test_footer_legal_links_present(self):
        response = self.client.get(reverse("core:home"))
        self.assertContains(response, reverse("core:legal_notice"))
        self.assertContains(response, reverse("core:privacy_policy"))

    def test_only_active_services_in_context(self):
        active = Service.objects.create(
            title="Actif",
            slug="actif",
            short_description="Service actif.",
            description="Description.",
        )
        Service.objects.create(
            title="Inactif",
            slug="inactif",
            short_description="Service inactif.",
            description="Description.",
            is_active=False,
        )
        response = self.client.get(reverse("core:home"))
        self.assertEqual(list(response.context["services"]), [active])

    def test_only_published_featured_projects_in_context(self):
        category = ProjectCategory.objects.create(name="Sites", slug="sites")
        featured = Project.objects.create(
            title="Publié et mis en avant",
            slug="publie-mis-en-avant",
            short_description="Projet visible.",
            description="Description.",
            category=category,
            featured_image="portfolio/sample.jpg",
            is_published=True,
            is_featured=True,
        )
        Project.objects.create(
            title="Publié seulement",
            slug="publie-seulement",
            short_description="Non mis en avant.",
            description="Description.",
            category=category,
            featured_image="portfolio/sample.jpg",
            is_published=True,
        )
        response = self.client.get(reverse("core:home"))
        self.assertEqual(list(response.context["featured_projects"]), [featured])

    def test_only_published_featured_products_in_context(self):
        featured = Product.objects.create(
            name="Produit visible",
            slug="produit-visible",
            short_description="Produit publié et mis en avant.",
            description="Description.",
            is_published=True,
            is_featured=True,
        )
        Product.objects.create(
            name="Produit masqué",
            slug="produit-masque",
            short_description="Produit non publié.",
            description="Description.",
            is_featured=True,
        )
        response = self.client.get(reverse("core:home"))
        self.assertEqual(list(response.context["featured_products"]), [featured])

    def test_testimonials_section_hidden_without_testimonials(self):
        response = self.client.get(reverse("core:home"))
        self.assertNotContains(response, "Ils font confiance à BBK Digital")


class StaticPagesTests(TestCase):
    """Tests des pages à propos et légales."""

    def test_about_page(self):
        response = self.client.get(reverse("core:about"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/about.html")
        self.assertContains(response, "À propos de BBK Digital")

    def test_legal_notice_page(self):
        response = self.client.get(reverse("core:legal_notice"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/legal_notice.html")
        self.assertContains(response, "Mentions légales")

    def test_privacy_policy_page(self):
        response = self.client.get(reverse("core:privacy_policy"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "core/privacy_policy.html")
        self.assertContains(response, "Politique de confidentialité")


class ErrorPagesTests(TestCase):
    """Tests des pages d'erreurs personnalisées."""

    def test_404_page(self):
        response = self.client.get("/page-inexistante/")
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, "errors/404.html")
        self.assertContains(response, "Page introuvable", status_code=404)

    def test_500_view(self):
        request = RequestFactory().get("/")
        response = server_error(request)
        self.assertEqual(response.status_code, 500)
