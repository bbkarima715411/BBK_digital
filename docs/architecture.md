# Architecture — BBK Digital

## Vue d'ensemble

Le projet suit une architecture Django modulaire de type "apps métier",
pensée pour évoluer sur plusieurs années.

## Décisions techniques

### 1. `config/` au lieu du nom du projet

Le dossier de configuration est nommé `config` : neutre, standard dans les
projets professionnels, et découplé du nom commercial du produit.

### 2. Settings découpés (`config/settings/`)

- `base.py` : configuration commune (apps, middleware, templates, i18n).
- `development.py` : DEBUG, debug-toolbar, emails en console.
- `production.py` : sécurité (HSTS, cookies), whitenoise, SMTP réel.

Les secrets sont lus depuis `.env` via `python-decouple`. Aucun secret versionné.

### 3. `apps/` — un domaine métier par application

| App         | Responsabilité                                        |
|-------------|-------------------------------------------------------|
| `core`      | Accueil, à propos, mentions légales, confidentialité  |
| `services`  | Catalogue des services (stockés en base)              |
| `portfolio` | Réalisations (titre, image, technologies, liens…)     |
| `products`  | Produits numériques BBK Digital — prévu pour le futur |
| `contact`   | Formulaire de contact sécurisé + envoi SMTP           |

### 4. Templates globaux

`templates/` à la racine (et non par app) pour centraliser `base.html`,
les includes (`navbar.html`, `footer.html`, `messages.html`) et les pages.
Toutes les pages héritent de `base.html` — zéro duplication.

### 5. CSS modulaire

`static/css/main.css` importe des fichiers découpés par rôle :

- `base/` : reset, variables (palette premium), typography
- `layout/` : navbar, footer, grid
- `components/` : buttons, cards, forms
- `pages/` : home, services, portfolio, contact

### 6. JavaScript

Fichiers dédiés dans `static/js/` (`main.js`, `navbar.js`, `animations.js`,
`contact-form.js`). Jamais de JS inline dans les templates.

## Charte graphique

| Variable            | Rôle                        |
|---------------------|-----------------------------|
| `--color-black`     | Couleur dominante           |
| `--color-anthracite`| Fonds secondaires, textes   |
| `--color-terracotta`| Couleur principale (marque) |
| `--color-gold`      | Accent uniquement           |
| `--color-ivory`     | Fonds clairs, textes sur foncé |

Typographies : **Cormorant Garamond** (titres), **Inter** (texte).
Design minimaliste, intemporel, coins légèrement arrondis, peu d'ombres.

## Étapes du projet

1. ✅ Architecture
2. Configuration Django
3. Applications
4. Modèles
5. Templates
6. Design
7. Fonctionnalités
