# Révision Histoire – Dates du Brevet

Application web permettant de réviser les principales dates du programme d'Histoire du Brevet des collèges sous forme de quiz interactif.

## Fonctionnalités

- Révision par chapitre.
- Questions présentées dans un ordre aléatoire.
- Saisie libre de la date.
- Vérification immédiate de la réponse.
- Possibilité d'afficher la bonne réponse.
- Score affiché en temps réel.
- Bilan final à la fin du quiz.

---

## Structure du projet

```
Projet/
│
├── index.html
├── style.css
├── script.js
└── README.md
```

---

## Technologies utilisées

- HTML5
- CSS3
- JavaScript (Vanilla)

Aucune bibliothèque externe n'est nécessaire.

---

## Fonctionnement

Au lancement de l'application :

1. L'utilisateur choisit un chapitre.
2. Les dates du chapitre sont mélangées aléatoirement.
3. Les questions sont affichées une par une.
4. L'utilisateur saisit la date correspondante.
5. Une correction immédiate indique si la réponse est correcte.
6. Le score est mis à jour après chaque question.
7. Un récapitulatif final est affiché lorsque toutes les questions ont été répondues.

---

## Chapitres disponibles

Le quiz couvre les principaux thèmes du programme d'Histoire de 3ᵉ :

- La Première Guerre mondiale
- Les régimes totalitaires : l'URSS de Staline
- Les régimes totalitaires : l'Allemagne nazie
- La France entre les deux guerres
- La Seconde Guerre mondiale
- La France défaite et occupée
- Les indépendances et la décolonisation
- La Guerre froide
- La construction européenne
- Les enjeux et conflits depuis 1989

---

## Types de réponses

Selon la question, plusieurs formats de dates peuvent être demandés :

- Année
- Mois + année
- Jour + mois + année
- Période (début – fin)

Le format attendu est indiqué sous chaque question.

---

## Fonctionnalités du quiz

- Vérification automatique de la réponse.
- Affichage de la bonne réponse en cas d'erreur.
- Bouton **Voir la réponse** disponible à tout moment.
- Affichage du score pendant toute la partie.
- Mélange automatique des questions à chaque nouvelle session.

---

## Personnalisation

Le fichier `script.js` permet facilement de :

- ajouter de nouveaux chapitres ;
- compléter les listes de dates ;
- modifier les réponses attendues ;
- adapter le fonctionnement du quiz.

L'apparence de l'application peut être personnalisée dans `style.css`.

---

## Lancer le projet

Ouvrir simplement le fichier :

```
index.html
```

dans un navigateur web.

Aucune installation ni serveur n'est nécessaire.

---

## Objectif pédagogique

Cette application a pour objectif d'aider les élèves de 3ᵉ à mémoriser les principales dates du programme d'Histoire grâce à un entraînement interactif et rapide en vue du Brevet des collèges.

---

## Auteur

Projet réalisé par Alexandre Coussediere pour proposer un outil simple et interactif de révision des dates essentielles du programme d'Histoire du Brevet.
