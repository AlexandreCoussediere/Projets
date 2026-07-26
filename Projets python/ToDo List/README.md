# Gestionnaire de tâches

Un gestionnaire de tâches développé en **Python**. Ce programme permet d'ajouter, consulter, modifier et supprimer des tâches, tout en sauvegardant automatiquement les données dans un fichier **JSON**.

---

## Description

- Ajouter une nouvelle tâche.
- Définir une priorité (basse, moyenne ou haute).
- Définir un statut (à faire, en cours ou terminée).
- Afficher la liste des tâches.
- Modifier le statut d'une tâche.
- Supprimer une tâche.
- Sauvegarder automatiquement les tâches dans un fichier `tasks.json`.
- Charger les tâches existantes au démarrage du programme.

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

Téléchargez les fichiers `To-Do List.py` et `tasks.json`, puis exécutez :

```bash
python To-Do List.py
```

ou

```bash
python3 To-Do List.py
```

Si le fichier `tasks.json` n'existe pas, il sera créé automatiquement lors de la première sauvegarde.

---

## Utilisation

Au lancement, un menu s'affiche :

```text
1. Ajouter une tâche
2. Afficher les tâches
3. Changer le statut d'une tâche
4. Supprimer une tâche
5. Quitter
```

Vous pouvez ensuite :

1. Ajouter une nouvelle tâche en indiquant sa description, sa priorité et son statut.
2. Consulter toutes les tâches enregistrées.
3. Modifier le statut d'une tâche existante.
4. Supprimer une tâche après confirmation.
5. Quitter le programme en sauvegardant automatiquement les tâches.

---

## Structure du projet

```text
.
├── gestionnaire_taches.py
├── tasks.json
└── README.md
```

---

## Technologies utilisées

- Python 3
- Module standard `json`

---

## Exemple

```text
Menu :

1. Ajouter une tâche
2. Afficher les tâches
3. Changer le statut d'une tâche
4. Supprimer une tâche
5. Quitter

Entrez votre choix (1-5) : 1

Entrez la description de la tâche : Finir le projet Python
Entrez le niveau de priorité de la tâche (basse/moyenne/haute) : haute
Entrez le statut de la tâche (à faire/terminée/en cours) : à faire
```

---

## Fichier `tasks.json`

Les tâches sont enregistrées dans un fichier nommé `tasks.json`. Ce fichier est chargé automatiquement au démarrage du programme et mis à jour lors des modifications ou lorsque vous quittez l'application.

Exemple de contenu :

```json
[
    {
        "description": "Finir le projet Python",
        "priorité": "haute",
        "statut": "en cours"
    },
    {
        "description": "Faire les courses",
        "priorité": "moyenne",
        "statut": "à faire"
    }
]
```

---

## Améliorations possibles

- Modifier la description ou la priorité d'une tâche.
- Rechercher une tâche par mot-clé.
- Trier les tâches par priorité ou par statut.
- Ajouter une date d'échéance.
- Filtrer les tâches selon leur statut.
- Développer une interface graphique avec Tkinter ou PyQt.
- Ajouter une sauvegarde automatique après chaque ajout de tâche.

---

## Auteur

Projet réalisé par Alexandre Coussediere dans le cadre d'un exercice d'apprentissage de **Python**.
