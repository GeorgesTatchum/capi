# capi

Programme de simulation de pocker planning en environnement agile# Application de Planning Poker

## Introduction

L'objectif de cette application est de permettre à des joueurs de participer à une session de planning poker, en respectant les règles définies. L'application est utilisée en mode local dans un premier temps (tous les joueurs utilisent une interface commune)

## Fonctionnalités

- **Configuration des joueurs** : Définir le nombre de joueurs et leurs pseudos.
- **Choix des règles** : Sélectionner parmi différentes règles de planning poker (strictes, moyenne, médiane, majorité absolue, majorité relative).
- **Gestion du backlog** : Entrer une liste de fonctionnalités (backlog) en JSON.
- **Vote et validation** : Les joueurs votent pour estimer la difficulté des fonctionnalités. La validation se fait selon les règles choisies.
- **Sauvegarde et reprise** : Enregistrer l'état d'avancement du backlog et reprendre une partie ultérieurement.

## Installation

### Prérequis

- Python 3.8 ou supérieur

### Backend

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/GeorgesTatchum/capi.git
   cd capi/backend
   ```

2. Installer les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Lancer le serveur :
   ```bash
   uvicorn app.main:app --reload
   ```

### Frontend

Le frontend utilise des templates Jinja2 et est servi par le backend FastAPI. Aucune installation supplémentaire n'est nécessaire.

## Utilisation

1. Accéder à l'application via votre navigateur à l'adresse `http://localhost:8000`.
2. Configurer le nombre de joueurs, leurs pseudos et les règles de jeu.
3. Entrer le backlog des fonctionnalités. [X = un backlog à entré statiquement dans le dossier backend/]
4. Commencer la session de planning poker et voter pour chaque fonctionnalité.
5. Sauvegarder automatiquement l'état d'avancement.

## Tests

Des tests unitaires sont fournis pour vérifier le bon fonctionnement des règles de jeu et de la logique de l'application.

### Exécuter les tests

1. Aller dans le répertoire `backend` :

   ```bash
   cd backend
   ```

2. Lancer les tests avec `pytest` :
   ```bash
   pytest
   ```

## Intégration Continue

L'intégration continue est configurée avec GitHub Actions. Les tests sont exécutés automatiquement à chaque push ou pull request.

### Configuration CI

Le fichier de configuration CI se trouve dans `.github/workflows/ci.yml`.

## Contribution

Les contributions sont les bienvenues ! Veuillez soumettre une pull request ou ouvrir une issue pour discuter des changements que vous souhaitez apporter.
