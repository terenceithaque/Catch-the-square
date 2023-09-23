# Script principal du jeu
import pygame  # Importer pygame
import pygame_menu  # Importer pygame_menu pour créer un menu principal
from pygame_menu import themes
pygame.init()


def game():
    "Lancer le jeu"
    pass


def go_back_mainmenu():
    "Retourner au menu principal"
    parameters._open(mainmenu)  # Ouvrir le menu principal


screen_width = 800  # Hauteur de la fenêtre de jeu
screen_height = 600  # Largeur de la fenêtre de jeu
screen = pygame.display.set_mode(
    (screen_width, screen_height))  # Créer une fenêtre de jeu
# La fenêtre de jeu s'intitule "Catch the square !"
pygame.display.set_caption("Catch the square !")

mainmenu = pygame_menu.Menu(
    "Menu principal", screen_width, screen_height, theme=themes.THEME_BLUE)  # Créer le menu principal du jeu.


mainmenu.mainloop(screen)  # Démarrer le menu principal
