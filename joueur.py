# Joueur
import pygame


class Joueur:
    "Joueur"

    def __init__(self):
        # Score du joueur. Equivaut au nombre de clics effectués sur le carré.
        self.score = 0
        # Fichier dans le lequel le meilleur score est enregistré
        self.fichier_score = "score.txt"
        with open(self.fichier_score, "r") as rf:  # Lire le meilleur score obtenu. rf = read file
            self.best_score = int(rf.read())

    def augmenter_score(self, montant):
        "Augmenter le score du joueur"
        self.score += montant  # Augmenter le score
        self.mettre_a_jour_meilleur_score()  # Mettre à jour le meilleur score

    def mettre_a_jour_meilleur_score(self):
        "Mettre à jour le meilleur score du joueur"
        if self.best_score < self.score:  # Si le meilleur score est inférieur au score actuel
            self.best_score = self.score  # Mettre à jour le meilleur score

    def save_score(self):
        "Sauvergarder le meilleur score dans un fichier"
        if self.score > self.best_score:
            # Ouvrir le fichier contenant le meilleur score en écriture. wf = write file
            with open(self.fichier_score, "w") as wf:

                wf.write(str(self.score))  # Ecrire le score actuel
                wf.close()  # Fermer le fichier quand l'opération d'écriture est terminée

        else:
            # Ouvrir le fichier contenant le meilleur score en écriture. wf = write file
            with open(self.fichier_score, "w") as wf:
                wf.write(str(self.best_score))  # Ecrire le meilleur score
                wf.close()  # Fermer le fichier quand l'opération d'écriture est finie
