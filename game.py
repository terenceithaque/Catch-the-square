# Script pour le déroulement d'une partie
import pygame  # Importer pygame
from tkinter import messagebox
from carre import *
from joueur import *
from joueurs import *
from pause import *
from threading import Timer
pygame.init()  # Initialiser pygame
pygame.display.init()


screen_width = 800  # Hauteur de l'écran
screen_height = 600  # Largeur de l'écran

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the square !")


def ask_quit():
    "Demander au joueur s'il souhaite arrêter la partie"
    ask = messagebox.askquestion(
        "Arrêter la partie en cours ?", "Souhaitez-vous vraiment quitter la partie en cours ?")
    return ask


def game():
    "Démarrer une nouvelle partie"
    carre = Carre(screen_width, screen_height)
    pseudo = entrer_pseudo()
    creer_dossier()  # Créer un dossier au nom du joueur s'il n'existe pas encore
    fichier_score = creer_fichier_score()
    joueur = Joueur(pseudo=pseudo, fichier_score=fichier_score)

    GAME_OVER = pygame.USEREVENT + 1
    duree_partie = 1000 * 120  # Durée de la partie convertie en secondes
    pygame.time.set_timer(GAME_OVER, duree_partie)

    pygame.display.flip()
    running = True  # Est-ce que le jeu est en cours d'exécution ?
    while running:
        print("Temps restant :", duree_partie / 1000)
        screen.fill((0, 0, 0))

        keys = pygame.key.get_pressed()  # Obtenir toutes les touches pressées par le joueur
        carre.move(screen)
        pause(keys)
        # carre.draw(screen)
        for event in pygame.event.get():  # Pour chaque évènement intercepté durant l'exécution du jeu
            # Si le joueur veut quitter le jeu
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                if ask_quit() == "yes":
                    running = False

                else:
                    continue

            elif event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
                joueur.update_clics()  # Mettre à jour le nombre total de clics
                # Obtenir la position du curseur de la souris
                pos_souris = pygame.mouse.get_pos()

                if carre.rect.collidepoint(pos_souris):
                    # print("Vous avez cliqué sur le carré !")
                    # Augmenter le score d'1 point.
                    joueur.augmenter_score(montant=1)
                    print(joueur.score)

                    joueur.save_score()

            elif event.type == GAME_OVER:
                game_over_time = Timer(5.0, joueur.game_over(screen, screen_width,
                                                             screen_height, delai=5000))

                game_over_time.start()

                running = False

        joueur.display_score(screen)
        joueur.display_clics(screen)
        joueur.afficher_pseudo(screen)

        pygame.display.flip()


game()  # Lancer le jeu
