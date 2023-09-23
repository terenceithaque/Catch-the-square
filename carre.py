# Carré sur lequel le joueur doit cliquer
import pygame
from random import randint


class Carre:
    "Carré"

    def __init__(self):
        self.width = 25  # Longueur du carré
        self.height = 25  # Largeur du carré
        self.speed = randint(4, 6)  # Vitesse de déplacement du carré
        self.rect = pygame.Rect(100, 100, self.width, self.height)
        self.color = (0, 0, 255)  # Couleur du carré

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
