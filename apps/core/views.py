"""Vues de l'application core : accueil, à propos, pages légales."""
from django.views.generic import TemplateView


class HomeView(TemplateView):
    """Page d'accueil du site BBK Digital."""

    template_name = "pages/home.html"


class AboutView(TemplateView):
    """Page de présentation du studio."""

    template_name = "pages/about.html"


class LegalNoticeView(TemplateView):
    """Mentions légales."""

    template_name = "pages/legal_notice.html"


class PrivacyPolicyView(TemplateView):
    """Politique de confidentialité."""

    template_name = "pages/privacy_policy.html"
