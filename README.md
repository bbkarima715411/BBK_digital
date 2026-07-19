# BBK Digital

Studio de conception de solutions numériques — sites web professionnels, applications web, outils métiers, automatisations, SaaS et produits numériques propres.

## Stack technique

- **Backend** : Python 3 / Django
- **Base de données** : PostgreSQL
- **Frontend** : HTML5, CSS3, JavaScript ES6
- **Configuration** : python-decouple + fichier `.env`

## Architecture

```
BBK_digital/
├── config/                 # Configuration du projet Django
│   └── settings/           # Settings séparés : base / development / production
├── apps/                   # Applications métier
│   ├── core/               # Accueil, à propos, pages légales
│   ├── services/           # Services proposés par le studio
│   ├── portfolio/          # Réalisations
│   ├── products/           # Produits numériques BBK Digital (évolutif)
│   └── contact/            # Formulaire de contact
├── templates/              # Templates HTML globaux (base, includes, pages)
├── static/
│   ├── css/
│   │   ├── base/           # reset, variables, typography
│   │   ├── layout/         # navbar, footer, grid
│   │   ├── components/     # buttons, cards, forms
│   │   └── pages/          # home, services, portfolio, contact
│   ├── js/                 # main, navbar, animations, contact-form
│   ├── images/
│   └── icons/
├── media/                  # Fichiers uploadés (portfolio, produits)
├── tests/                  # Tests transverses
├── docs/                   # Documentation du projet
└── requirements/           # Dépendances : base / development / production
```

## Installation (développement)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements/development.txt
copy .env.example .env      # puis renseigner les valeurs
python manage.py migrate
python manage.py runserver
```

## Conventions

- PEP8 et conventions Django respectées.
- Aucun secret dans le code : tout passe par `.env`.
- CSS modulaire importé via `static/css/main.css`.
- JavaScript uniquement dans `static/js/` — jamais inline dans les templates.
