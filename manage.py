#!/usr/bin/env python
"""Utilitaire en ligne de commande de Django pour le projet BBK Digital."""
import os
import sys


def main():
    """Point d'entrée des commandes d'administration Django."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Impossible d'importer Django. Est-il installé et disponible "
            "dans votre environnement virtuel ? L'avez-vous activé ?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
