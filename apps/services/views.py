"""Vues de l'application services."""
from django.views.generic import ListView

from .models import Service


class ServiceListView(ListView):
    """Liste des services actifs, dans l'ordre d'affichage défini."""

    model = Service
    template_name = "services/service_list.html"
    context_object_name = "services"

    def get_queryset(self):
        """Seuls les services actifs sont affichés publiquement."""
        return Service.objects.filter(is_active=True)
