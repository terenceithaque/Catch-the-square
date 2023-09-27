# Joueur
import pygame


class Joueur:
    "Joueur"

    def __init__(self, pseudo, fichier_score):
        # Score du joueur. Equivaut au nombre de clics effectués sur le carré.
        self.score = 0

        self.score_font = pygame.font.Font(None, 36)
        self.best_score_font = pygame.font.Font(None, 36)

        self.clics = 0  # Nombre total de clics effectués par le joueur, y compris en dehors du carré

        self.clics_font = pygame.font.Font(None, 36)

        self.pseudo = pseudo  # Pseudo du joueur

        # Fichier dans le lequel le meilleur score est enregistré
        self.fichier_score = fichier_score
        print(self.pseudo)

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

    def display_score(self, screen):
        "Afficher le score et le meilleur score à l'écran"
        score_text = self.score_font.render(
            f"Score : {self.score}", True, (255, 255, 255))

        best_score_text = self.score_font.render(
            f"Meilleur score : {self.best_score}", True, (255, 255, 255))

       # screen.fill((0, 0, 0))

        screen.blit(score_text, (0, 0))
        screen.blit(best_score_text, (0, 20))

    def display_clics(self, screen):
        "Afficher le nombre total de clics effectués par le joueur"
        clics_text = self.clics_font.render(
            f"Total clics : {self.clics}", True, (255, 255, 255))

        screen.blit(clics_text, (0, 40))

    def update_clics(self):
        "Mettre à jour le nombre de clics"
        self.clics += 1
