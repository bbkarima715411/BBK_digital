"""Vues de l'application portfolio."""
from django.views.generic import ListView

from .models import Project


class ProjectListView(ListView):
    """Liste des réalisations publiées, dans l'ordre d'affichage défini."""

    model = Project
    template_name = "portfolio/project_list.html"
    context_object_name = "projects"

    def get_queryset(self):
        """Seuls les projets publiés sont affichés publiquement."""
        return (
            Project.objects.filter(is_published=True)
            .select_related("category")
            .prefetch_related("technologies")
        )
