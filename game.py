# Script pour le déroulement d'une partie
import pygame  # Importer pygame
from tkinter import messagebox
from carre import *
pygame.init()  # Initialiser pygame


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
    screen.fill((0, 0, 0))
    carre = Carre()
    carre.draw(screen)
    pygame.display.flip()
    running = True  # Est-ce que le jeu est en cours d'exécution ?
    while running:
        keys = pygame.key.get_pressed()  # Obtenir toutes les touches pressées par le joueur

        for event in pygame.event.get():  # Pour chaque évènement intercepté durant l'exécution du jeu
            # Si le joueur veut quitter le jeu
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                if ask_quit() == "yes":
                    running = False

                else:
                    continue

            elif event.type == pygame.MOUSEBUTTONUP and event.button == pygame.BUTTON_LEFT:
                # Obtenir la position du curseur de la souris
                pos_souris = pygame.mouse.get_pos()
                if carre.rect.collidepoint(pos_souris):
                    print("Vous avez cliqué sur le carré !")

    pygame.display.flip()


game()
