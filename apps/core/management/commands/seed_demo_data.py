"""Commande de gestion : insertion de données de démonstration.

Usage : python manage.py seed_demo_data

À n'utiliser qu'en développement. La commande est idempotente :
elle n'insère rien si les données existent déjà (get_or_create).
"""
from django.core.management.base import BaseCommand

from apps.portfolio.models import ProjectCategory, Technology
from apps.services.models import Service

SERVICES = [
    ("Création de sites", "creation-de-sites", "Sites web professionnels sur mesure."),
    ("Applications web", "applications-web", "Applications web robustes et évolutives."),
    ("Développement sur mesure", "developpement-sur-mesure", "Outils métiers adaptés à vos besoins."),
    ("Automatisation", "automatisation", "Automatisation de vos processus répétitifs."),
    ("Maintenance", "maintenance", "Suivi, sécurité et évolutions de vos solutions."),
    ("SaaS", "saas", "Conception de solutions SaaS durables."),
]

CATEGORIES = [
    ("Sites web", "sites-web"),
    ("Applications web", "applications-web"),
    ("Outils métiers", "outils-metiers"),
    ("Automatisations", "automatisations"),
]

TECHNOLOGIES = [
    ("Python", "python"),
    ("Django", "django"),
    ("PostgreSQL", "postgresql"),
    ("JavaScript", "javascript"),
    ("HTML5", "html5"),
    ("CSS3", "css3"),
]


class Command(BaseCommand):
    """Insère les données de démonstration (services, catégories, technologies)."""

    help = "Insère des données de démonstration pour le développement."

    def handle(self, *args, **options):
        created_count = 0

        for order, (title, slug, short_description) in enumerate(SERVICES):
            _, created = Service.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title,
                    "short_description": short_description,
                    "description": short_description,
                    "display_order": order,
                },
            )
            created_count += created

        for order, (name, slug) in enumerate(CATEGORIES):
            _, created = ProjectCategory.objects.get_or_create(
                slug=slug,
                defaults={"name": name, "display_order": order},
            )
            created_count += created

        for name, slug in TECHNOLOGIES:
            _, created = Technology.objects.get_or_create(
                slug=slug, defaults={"name": name}
            )
            created_count += created

        self.stdout.write(
            self.style.SUCCESS(f"Données de démonstration : {created_count} objet(s) créé(s).")
        )
