import json

tache = []

def ajouter_tache():
    # Demander la description
    description = input("Entrez la description de la tâche : ")

    # Demander la priorité avec vérification
    while True:
        priorite = input("Entrez le niveau de priorité de la tâche (basse/moyenne/haute) : ").lower()
        if priorite in ["basse", "moyenne", "haute"]:
            break
        print("Veuillez entrer une valeur valide (basse/moyenne/haute).")

    # Demander le statut avec vérification
    while True:
        statut = input("Entrez le statut de la tâche (à faire/terminée/en cours) : ").lower()
        if statut in ["à faire", "terminée", "en cours"]:
            break
        print("Veuillez entrer une valeur valide (à faire/terminée/en cours).")

    # Ajouter la tâche à la liste
    tache.append(
      {
        "description": description,
        "priorité": priorite,
        "statut": statut
      }
)

def afficher_taches():
    if not tache:  # Vérifie si la liste est vide
        print("Aucune tâche n'a été ajoutée pour le moment.")
    else:
        print("\nListe des tâches :")
        for index, t in enumerate(tache, start=1):  # Enumerate pour afficher un numéro
            print(f"\nTâche {index}:")
            print(f"  - Description : {t['description']}")
            print(f"  - Priorité : {t['priorité']}")
            print(f"  - Statut : {t['statut']}")
def changer_statut():
    if not tache:
        print("Aucune tâche n'a été ajoutée pour le moment.")
        return

    # Afficher les tâches existantes pour que l'utilisateur choisisse
    afficher_taches()
    print("\n")

    # Demander à l'utilisateur de choisir une tâche
    try:
        choix = int(input("Entrez le numéro de la tâche à modifier : "))
        if choix < 1 or choix > len(tache):
            print("Numéro de tâche invalide. Veuillez réessayer.")
            return
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return

    # Afficher les statuts possibles (ajout de "en cours")
    print("\nStatuts disponibles :")
    print("1. à faire")
    print("2. terminée")
    print("3. en cours")  # Ajout de cette option

    # Demander à l'utilisateur de choisir un nouveau statut
    try:
        statut_choix = int(input("Entrez le numéro du nouveau statut : "))
        if statut_choix == 1:
            nouveau_statut = "à faire"
        elif statut_choix == 2:
            nouveau_statut = "terminée"
        elif statut_choix == 3:
            nouveau_statut = "en cours"  # Ajout de cette option
        else:
            print("Numéro de statut invalide. Veuillez réessayer.")
            return
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return

    # Mettre à jour le statut de la tâche
    tache[choix - 1]["statut"] = nouveau_statut
    print(f"Le statut de la tâche '{tache[choix - 1]['description']}' a été mis à jour en '{nouveau_statut}'.")
    sauvegarder_taches()  # Sauvegarde après la modification

def supprimer_tache():
    if not tache:
        print("Aucune tâche n'a été ajoutée pour le moment.")
        return

    # Afficher les tâches existantes pour que l'utilisateur choisisse
    afficher_taches()
    print("\n")

    # Demander à l'utilisateur de choisir une tâche à supprimer
    try:
        choix = int(input("Entrez le numéro de la tâche à supprimer : "))
        if choix < 1 or choix > len(tache):
            print("Numéro de tâche invalide. Veuillez réessayer.")
            return
    except ValueError:
        print("Veuillez entrer un numéro valide.")
        return

    # Confirmer la suppression
    confirmation = input(f"Voulez-vous vraiment supprimer la tâche '{tache[choix - 1]['description']}' ? (oui/non) : ").lower()
    if confirmation != "oui":
        print("Suppression annulée.")
        return

    # Supprimer la tâche
    tache_supprimee = tache.pop(choix - 1)
    print(f"La tâche '{tache_supprimee['description']}' a été supprimée avec succès.")
    sauvegarder_taches()  # Sauvegarde après la suppression

def sauvegarder_taches(nom_fichier="tasks.json"):
    """Sauvegarde les tâches dans un fichier JSON."""
    with open(nom_fichier, "w", encoding="utf-8") as fichier:
        json.dump(tache, fichier, indent=4, ensure_ascii=False)
    print(f"Tâches sauvegardées dans {nom_fichier}.")

def charger_taches(nom_fichier="tasks.json"):
    """Charge les tâches depuis un fichier JSON."""
    global tache
    try:
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            tache = json.load(fichier)
        print(f"Tâches chargées depuis {nom_fichier}.")
    except FileNotFoundError:
        print(f"Le fichier {nom_fichier} n'existe pas encore. Une nouvelle liste de tâches sera créée.")
        tache = []
    except json.JSONDecodeError:
        print(f"Le fichier {nom_fichier} est corrompu. Une nouvelle liste de tâches sera créée.")
        tache = []

def quitter():
    """Quitte le programme après avoir sauvegardé les tâches."""
    confirmation = input("Voulez-vous vraiment quitter ? Toutes les tâches seront sauvegardées. (oui/non) : ").lower()
    if confirmation == "oui":
        sauvegarder_taches()
        print("Au revoir !")
        exit()
    else:
        print("Retour au menu principal.")

charger_taches()
while True:
    print("\nMenu :")
    print("1. Ajouter une tâche")
    print("2. Afficher les tâches")
    print("3. Changer le statut d'une tâche")
    print("4. Supprimer une tâche")
    print("5. Quitter")

    choix_menu = input("Entrez votre choix (1-5) : ")

    if choix_menu == "1":
        ajouter_tache()
    elif choix_menu == "2":
        afficher_taches()
    elif choix_menu == "3":
        changer_statut()
    elif choix_menu == "4":
        supprimer_tache()
    elif choix_menu == "5":
        quitter()
    else:
        print("Choix invalide. Veuillez réessayer.")