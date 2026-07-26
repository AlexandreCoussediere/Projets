# Révision Brevet Maths

Application web simple permettant de s'entraîner au Brevet de mathématiques grâce à des exercices tirés aléatoirement.

## Fonctionnalités

- Banque de **50 exercices** de niveau 3e.
- Sélection aléatoire de **3 exercices** à chaque série.
- Affichage de la correction sur demande.
- Suivi automatique de la progression grâce au **LocalStorage**.
- Système de niveaux selon le nombre de corrections consultées.
- Interface responsive compatible ordinateur, tablette et mobile.

---

## Structure du projet

```
Projet/
│
├── index.html
├── style.css
├── script.js
├── README.md
│
└── images/
    ├── pythagore.svg
    └── thales.svg
```

---

## Technologies utilisées

- HTML5
- CSS3
- JavaScript (Vanilla)

Aucune bibliothèque externe n'est nécessaire.

---

## Fonctionnement

Au chargement de la page :

- une nouvelle connexion est comptabilisée ;
- trois exercices sont choisis aléatoirement parmi la banque ;
- les statistiques enregistrées sont restaurées automatiquement.

Lorsque l'utilisateur affiche une correction :

- la correction apparaît ;
- elle n'est comptabilisée qu'une seule fois ;
- les données sont sauvegardées dans le navigateur.

---

## Statistiques enregistrées

L'application mémorise :

- nombre de corrections consultées
- nombre de connexions
- nombre de séries générées
- nombre total d'exercices affichés
- niveau de progression

Toutes ces informations sont enregistrées grâce au **LocalStorage**.

---

## Système de niveaux

| Corrections vues | Niveau |
|-----------------:|--------|
| 0 | Débutant |
| 10 | Novice |
| 25 | Intermédiaire |
| 50 | Bon niveau |
| 100 | Très bon niveau |
| 200 | Expert |
| 400 | Préparation Brevet ++ |

---

## Exercices disponibles

La banque couvre plusieurs chapitres du programme de 3e :

- Théorème de Pythagore
- Théorème de Thalès
- Pourcentages
- Fonctions
- Calcul littéral
- Équations
- Fractions
- Puissances
- Probabilités
- Statistiques
- Aires
- Volumes
- Trigonométrie
- Vitesse
- Proportionnalité

---

## Personnalisation

Il est très simple de :

- ajouter de nouveaux exercices dans le tableau `banque` du fichier `script.js` ;
- modifier les niveaux ;
- changer le nombre d'exercices affichés ;
- personnaliser le style dans `style.css`.

---

## Lancer le projet

Il suffit d'ouvrir le fichier :

```
index.html
```

dans un navigateur web.

---

## Auteur

Projet réalisé par Alexandre Coussediere pour proposer un outil simple de révision du Brevet des collèges en mathématiques.
