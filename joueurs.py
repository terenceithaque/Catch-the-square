"Gérer les différents joueurs"
from tkinter import Tk, simpledialog
import os


def entrer_pseudo():
    "Demander au joueur d'entrer son pseudo"
    root = Tk()  # Créer une fenêtre
    root.withdraw()
    global pseudo
    pseudo = simpledialog.askstring("Votre pseudo", "Saisissez votre pseudo :")
    return pseudo


def creer_dossier():
    "Créer un dossier au nom du joueur"
    global dossier_joueur
    dossier_joueur = os.path.join("joueurs", pseudo)
    if not os.path.exists(dossier_joueur):
        # Créer un dossier au nom du joueur si celui-ci n'existe pas
        os.makedirs(dossier_joueur)
        print(f"Dossier {dossier_joueur} créé")

    else:
        print(f"Dossier {dossier_joueur} déjà existant.")


def creer_fichier_score():
    "Créer un fichier contenant le score"
    chemin_fichier = os.path.join(dossier_joueur, "score.txt")

    if not os.path.isfile(chemin_fichier):
        with open(chemin_fichier, "w") as file:
            file.write(str(0))

    return chemin_fichier
