# Pygame Project

Un projet de jeu développé en **Python** avec la bibliothèque **Pygame**.  
Le programme contient un menu principal, une page d'options et un jeu de type **Snake** jouable avec le clavier.

---

## Description

Le projet est composé de plusieurs fichiers permettant de gérer différentes parties du jeu :

- Un menu principal avec navigation par boutons.
- Une musique de fond.
- Une interface graphique avec arrière-plan personnalisé.
- Un système de lancement du jeu depuis le menu.
- Une page d'options avec retour au menu principal.
- Un jeu Snake avec :
  - Déplacement du serpent.
  - Apparition aléatoire des pommes.
  - Système de score.
  - Détection des collisions.
  - Écran de défaite.
  - Possibilité de recommencer une partie.

---

## Fonctionnalités

### Menu principal (`main.py`)

- Affichage d'un écran d'accueil.
- Boutons interactifs :
  - Nouvelle partie.
  - Options.
  - Quitter.
- Effets visuels au survol des boutons.
- Chargement d'une image de fond.
- Lecture d'une musique de fond.

---

### Options (`game_options.py`)

- Interface d'options indépendante.
- Bouton permettant de revenir au menu principal.
- Conservation du même style graphique que le menu principal.

---

### Jeu Snake (`game.py`)

- Contrôle du serpent avec les touches directionnelles :
  - Flèche haut.
  - Flèche bas.
  - Flèche gauche.
  - Flèche droite.
- Déplacement automatique du serpent.
- Agrandissement du serpent lorsqu'il mange une pomme.
- Calcul du score.
- Gestion des collisions :
  - Avec les murs.
  - Avec le corps du serpent.
- Écran de fin de partie.
- Redémarrage avec la touche espace.

---

## Installation

### Prérequis

- Python 3.x
- Pygame

Vérifiez votre version de Python :

```bash
python --version
```

Installez Pygame avec :

```bash
pip install pygame
```

---

## Exécution

Placez-vous dans le dossier du projet puis lancez :

```bash
python main.py
```

Le menu principal s'affichera et permettra de démarrer une partie.

---

## Structure du projet

```text
.
├── main.py
├── game.py
├── game_options.py
├── assets
│   ├── fond.png
│   └── musique_de_fond.mp3
└── README.md
```

---

## Technologies utilisées

- Python 3
- Pygame
- Module standard :
  - `random`
  - `sys`
  - `os`
  - `subprocess`

---

## Contrôles du jeu

| Action | Touche |
|--------|--------|
| Déplacer le serpent vers le haut | Flèche haut |
| Déplacer le serpent vers le bas | Flèche bas |
| Déplacer le serpent vers la gauche | Flèche gauche |
| Déplacer le serpent vers la droite | Flèche droite |
| Recommencer après une défaite | Espace |

---

## Exemple de partie

```text
Score : 5


GAME OVER

Score : 5

Press space to Restart
```

---

## Améliorations possibles

- Ajouter plusieurs niveaux de difficulté.
- Augmenter progressivement la vitesse du serpent.
- Ajouter un système de meilleur score.
- Ajouter des effets sonores.
- Ajouter plusieurs modes de jeu.
- Ajouter une sauvegarde des scores.
- Ajouter une interface d'options plus complète.
- Ajouter des animations pour le serpent et les pommes.

---

## Auteur

Projet réalisé par Alexandre Coussediere dans le cadre d'un exercice d'apprentissage de **Python et de Pygame**.
