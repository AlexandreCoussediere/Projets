# Hangman.py

Un jeu du **Pendu** développé en **Python**. Le programme choisit un mot aléatoirement dans une liste de mots français et le joueur doit le deviner en proposant des lettres une par une avant d'épuiser ses vies.

---

## Description

- Sélection aléatoire d'un mot.
- Saisie d'une lettre à la fois.
- Vérification des lettres déjà proposées.
- Système de vies (5 vies au départ).
- Affichage de la progression du mot.
- Message de victoire ou de défaite.

---

## Installation

### Prérequis

- Python 3.x

Vérifiez votre version de Python :

```bash
python --version
```

ou

```bash
python3 --version
```

---

## Exécution

Téléchargez le fichier `Hangman.py`, puis exécutez :

```bash
python Hangman.py
```

ou

```bash
python3 Hangman.py
```

---

## Comment jouer

1. Le programme choisit un mot aléatoire.
2. Le mot est affiché sous forme de tirets (`_`).
3. À chaque tour, entrez une lettre.
4. Si la lettre est présente, elle est révélée dans le mot.
5. Sinon, vous perdez une vie.
6. Vous gagnez lorsque toutes les lettres du mot sont trouvées.
7. Vous perdez lorsque vous n'avez plus de vies.

---

## Structure du projet

```text
.
├── Hangman.py
└── README.md
```

---

## Technologies utilisées

- Python 3
- Module standard `random`

---

## Exemple

```text
Bienvenue dans le jeu du Pendu !
Devinez le mot en proposant des lettres une par une.

Mot à deviner : _ _ _ _ _

Lettres déjà proposées :

Il vous reste 5 vies

Proposez une lettre : e

Bonne proposition ! La lettre 'e' est dans le mot.
```

---

## Améliorations possibles

- Ajouter un dessin du pendu en ASCII.
- Permettre de deviner le mot complet.
- Ajouter plusieurs niveaux de difficulté.
- Charger les mots depuis un fichier texte.
- Afficher un score.
- Ajouter une interface graphique avec Tkinter ou Pygame.
- Gérer correctement les accents et les caractères spéciaux.

---

## Auteur

Projet réalisé par Alexandre Coussediere dans le cadre d'un exercice d'apprentissage de **Python**.
