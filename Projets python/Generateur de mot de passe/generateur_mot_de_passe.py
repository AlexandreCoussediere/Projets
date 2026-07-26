import random
import string

def generer_mot_de_passe(longueur: int, inclure_majuscules: bool = True, inclure_chiffres: bool = True, inclure_symboles: bool = True) -> str:
    # Validation des paramètres
    if longueur < 1:
        raise ValueError("La longueur doit être au moins égale à 1.")

    # Construction de la liste des caractères à utiliser
    caracteres = []

    # Toujours inclure les minuscules (a-z)
    caracteres.extend(string.ascii_lowercase)

    # Ajouter les autres types de caractères si demandés
    if inclure_majuscules:
        caracteres.extend(string.ascii_uppercase)
    if inclure_chiffres:
        caracteres.extend(string.digits)
    if inclure_symboles:
        caracteres.extend(string.punctuation)

    # Vérifier qu'au moins un type de caractère est sélectionné
    if not caracteres:
        raise ValueError("Au moins un type de caractère doit être sélectionné (majuscules, chiffres ou symboles).")

    # Générer le mot de passe en choisissant aléatoirement dans la liste des caractères
    mot_de_passe = [random.choice(caracteres) for _ in range(longueur)]

    # Retourner le mot de passe sous forme de chaîne
    return "".join(mot_de_passe)
# Interaction avec l'utilisateur
print("Générateur de mot de passe sécurisé")
print("----------------------------------")

# Demander la longueur du mot de passe
while True:
    try:
        longueur = int(input("Entrez la longueur du mot de passe (minimum 1) : "))
        if longueur < 1:
            print("La longueur doit être au moins égale à 1. Réessayez.")
            continue
        break
    except ValueError:
        print("Veuillez entrer un nombre valide.")

# Demander si l'utilisateur veut inclure des majuscules
while True:
    reponse = input("Inclure des majuscules ? (o/n) : ").strip().lower()
    if reponse in ("o", "n"):
        inclure_majuscules = (reponse == "o")
        break
    print("Veuillez répondre par 'o' ou 'n'.")

# Demander si l'utilisateur veut inclure des chiffres
while True:
    reponse = input("Inclure des chiffres ? (o/n) : ").strip().lower()
    if reponse in ("o", "n"):
        inclure_chiffres = (reponse == "o")
        break
    print("Veuillez répondre par 'o' ou 'n'.")

# Demander si l'utilisateur veut inclure des symboles
while True:
    reponse = input("Inclure des symboles ? (o/n) : ").strip().lower()
    if reponse in ("o", "n"):
        inclure_symboles = (reponse == "o")
        break
    print("Veuillez répondre par 'o' ou 'n'.")

# Générer le mot de passe
try:
    mot_de_passe = generer_mot_de_passe(
        longueur,
        inclure_majuscules,
        inclure_chiffres,
        inclure_symboles
    )
    print("\nMot de passe généré :", mot_de_passe)
except ValueError as e:
    print("Erreur :", e)
while True:
        reponse = input("\nVoulez-vous générer un autre mot de passe ? (o/n) : ").strip().lower()
        if reponse in ("o", "n"):
            if reponse == "n":
                print("Au revoir !")
                exit()
            break
        print("Veuillez répondre par 'o' ou 'n'.")