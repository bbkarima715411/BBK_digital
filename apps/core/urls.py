"""URLs de l'application core."""
from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("a-propos/", views.AboutView.as_view(), name="about"),
    path("mentions-legales/", views.LegalNoticeView.as_view(), name="legal_notice"),
    path(
        "politique-de-confidentialite/",
        views.PrivacyPolicyView.as_view(),
        name="privacy_policy",
    ),
]
