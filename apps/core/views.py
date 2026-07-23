"""Vues de l'application core : accueil, à propos, pages légales, erreurs."""
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.portfolio.models import Project
from apps.products.models import Product
from apps.services.models import Service


class HomeView(TemplateView):
    """Page d'accueil du site BBK Digital."""

    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        """Fournit les contenus publiés mis en avant sur la page d'accueil."""
        context = super().get_context_data(**kwargs)
        context["services"] = Service.objects.filter(is_active=True)[:6]
        context["featured_projects"] = (
            Project.objects.filter(is_published=True, is_featured=True)
            .select_related("category")[:3]
        )
        context["featured_products"] = Product.objects.filter(
            is_published=True, is_featured=True
        )[:3]
        return context


class AboutView(TemplateView):
    """Page de présentation du studio."""

    template_name = "core/about.html"


class LegalNoticeView(TemplateView):
    """Mentions légales."""

    template_name = "core/legal_notice.html"


class PrivacyPolicyView(TemplateView):
    """Politique de confidentialité."""

    template_name = "core/privacy_policy.html"


def page_not_found(request, exception):
    """Vue d'erreur 404 personnalisée."""
    return render(request, "errors/404.html", status=404)


def server_error(request):
    """Vue d'erreur 500 personnalisée."""
    return render(request, "errors/500.html", status=500)
