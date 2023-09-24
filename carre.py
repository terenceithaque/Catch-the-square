# Carré sur lequel le joueur doit cliquer
import pygame
from random import randint, random


class Carre(pygame.sprite.Sprite):
    "Carré"

    def __init__(self):
        self.width = 25  # Longueur du carré
        self.height = 25  # Largeur du carré
        # Charger l'image "square.jpg" pour représenter le carré à l'écran
        self.image = pygame.image.load("images\square.jpg")
        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        self.speed = randint(4, 6)  # Vitesse de déplacement du carré
        self.rect = self.image.get_rect()
        self.x = self.rect.x
        print(self.x)
        self.y = self.rect.y
        self.color = (0, 0, 255)  # Couleur du carré

    def move(self):
        "Déplacer le carré sur l'écran"
        direction = randint(-1, 1)
        self.x += direction * self.speed
        self.y += direction * self.speed

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
