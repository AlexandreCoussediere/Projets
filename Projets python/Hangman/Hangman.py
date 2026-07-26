import random

liste_mots = [
  "able", "acide", "aussi", "aire", "armée", "loin",
  "bébé", "dos", "balle", "groupe", "banque", "base",
  "bain", "poutre", "haricot", "ours", "battre", "été",
  "cloche", "ceinture", "meilleur", "facture", "oiseau", "souffler",
  "bleu", "bateau", "corps", "bouillir", "os", "livre",
  "botte", "ennuyer", "né", "patron", "les deux", "bol",
  "ampoule", "brûler", "appeler", "calme", "venir", "camp",
  "carte", "soin", "cas", "argent", "jeter", "cellule",
  "discuter", "puce", "ville", "frapper", "club", "charbon",
  "manteau", "code", "froid", "venir", "cuire", "frais",
  "affronter", "copier", "noyau", "coûter", "équipage", "récolte",
  "corbeau", "cube", "guérir", "boucler", "mignon", "humide",
  "oser", "sombre", "données", "date", "aube", "jours",
  "mort", "accord", "doyen", "cher", "dette", "profond",
  "cerf", "bureau", "composer", "dé", "mourir", "régime",
  "terrible", "terre", "plat", "disque", "faire", "chiens",
  "dôme", "porte", "en bas", "dessiner", "tirer", "goutte",
  "tambour", "canard", "terne", "muet", "poussière", "chaque",
  "gagner", "facilité", "est", "facile", "écho", "bord",
  "éditer", "œufs", "sortie", "visage", "fait", "disparaître",
  "échouer", "juste", "automne", "renommée", "ferme", "rapide",
  "destin", "peur", "exploit", "nourrir", "sentir", "pieds",
  "tomber", "ressentir", "peu", "fief", "figues", "dossier",
  "remplir", "film", "trouver", "fin", "feu", "ferme",
  "poisson", "poing", "cinq", "drapeau", "plat", "s'enfuir",
  "voler", "flux", "mousse", "gens", "tendre", "police",
  "nourriture", "idiot", "pied", "gué", "fourchette", "former",
  "fort", "sale", "quatre", "volaille", "libre", "de",
  "carburant", "plein", "fumée", "fonds", "gain", "jeu",
  "porte", "donner", "engrenage", "gène", "cadeau", "fille",
  "donner", "content", "vallée", "léger", "lueur", "bouillie",
  "briller", "colle", "but"
]  # Liste de tous les mots possibles à choisir

mot_secret = random.choice(liste_mots)  # Choix aléatoire d'un mot
lettres_proposees = []
vies_restantes = 5
mot_affiche = []

for i in range(len(mot_secret)):
    mot_affiche.append("_")

def afficher_etat():
    print("\nMot à deviner : " + " ".join(mot_affiche))
    print(f"Lettres déjà proposées : {', '.join(lettres_proposees)}")
    print(f"Il vous reste {vies_restantes} vies\n")

def proposer_lettre():
    while True:
        lettre = input("Proposez une lettre : ").lower()
        if len(lettre) != 1 or not lettre.isalpha():
            print("Veuillez entrer une seule lettre valide (a-z).")
        elif lettre in lettres_proposees:
            print("Vous avez déjà proposé cette lettre.")
        else:
            lettres_proposees.append(lettre)
            if lettre in mot_secret:
                for i in range(len(mot_secret)):
                    if mot_secret[i] == lettre:
                        mot_affiche[i] = lettre
                print(f"Bonne proposition ! La lettre '{lettre}' est dans le mot.")
            else:
                global vies_restantes
                vies_restantes -= 1
                print(f"Mauvaise proposition ! La lettre '{lettre}' n'est pas dans le mot.")
            break

print("Bienvenue dans le jeu du Pendu !")
print("Devinez le mot en proposant des lettres une par une.\n")

while vies_restantes > 0 and "_" in mot_affiche:
    afficher_etat()
    proposer_lettre()

if vies_restantes == 0:
    print(f"\nGame Over ! Vous avez perdu. Le mot était : {mot_secret}")
else:
    print(f"\nFélicitations ! Vous avez deviné le mot : {mot_secret}")