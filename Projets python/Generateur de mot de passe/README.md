# Générateur de mot de passe

Un générateur de mots de passe sécurisé développé en **Python**. Le programme permet de créer des mots de passe aléatoires en personnalisant leur longueur et les types de caractères à inclure.

---

## Description

- Génération aléatoire de mots de passe.
- Choix de la longueur du mot de passe.
- Possibilité d'inclure des lettres majuscules.
- Possibilité d'inclure des chiffres.
- Possibilité d'inclure des symboles.
- Vérification des entrées utilisateur.
- Génération de plusieurs mots de passe sans relancer le programme.

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

Téléchargez le fichier `generateur_mot_de_passe.py`, puis exécutez :

```bash
python generateur_mot_de_passe.py
```

ou

```bash
python3 generateur_mot_de_passe.py
```

---

## Utilisation

1. Choisissez la longueur du mot de passe.
2. Indiquez si vous souhaitez inclure :
   - des lettres majuscules ;
   - des chiffres ;
   - des symboles.
3. Le programme génère un mot de passe aléatoire selon vos choix.
4. Vous pouvez générer un nouveau mot de passe sans quitter le programme.

---

## Structure du projet

```text
.
├── generateur_mot_de_passe.py
└── README.md
```

---

## Technologies utilisées

- Python 3
- Module standard `random`
- Module standard `string`

---

## Exemple

```text
Générateur de mot de passe sécurisé
----------------------------------

Entrez la longueur du mot de passe (minimum 1) : 16
Inclure des majuscules ? (o/n) : o
Inclure des chiffres ? (o/n) : o
Inclure des symboles ? (o/n) : o

Mot de passe généré : T#8vLm!2Qx@5aPf$

Voulez-vous générer un autre mot de passe ? (o/n) :
```

---

## Améliorations possibles

- Garantir la présence d'au moins un caractère de chaque catégorie sélectionnée.
- Permettre de copier automatiquement le mot de passe dans le presse-papiers.
- Ajouter une estimation de la robustesse du mot de passe.
- Enregistrer les mots de passe dans un fichier chiffré.
- Développer une interface graphique avec Tkinter ou PyQt.
- Ajouter des options pour exclure certains caractères ambigus (ex. `0`, `O`, `l`, `I`).

---

## Auteur

Projet réalisé par Alexandre coussediere dans le cadre d'un exercice d'apprentissage de **Python**.
