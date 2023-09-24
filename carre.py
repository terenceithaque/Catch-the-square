# Carré sur lequel le joueur doit cliquer
import pygame
from random import randint, random


class Carre(pygame.sprite.Sprite):
    "Carré"

    def __init__(self, screen_width, screen_height):
        self.width = 25  # Longueur du carré
        self.height = 25  # Largeur du carré
        # Charger l'image "square.jpg" pour représenter le carré à l'écran
        self.image = pygame.image.load("images\square.jpg")
        self.image = pygame.transform.scale(
            self.image, (self.width, self.height))

        self.speed = randint(4, 6)  # Vitesse de déplacement du carré
        self.rect = self.image.get_rect()

        self.rect.x = screen_width / 2
        self.rect.y = screen_height / 2
        self.x = screen_width
        self.y = screen_height

        # print(self.rect)
        # self.x = self.rect.x
        # print(self.x)
        # self.y = self.rect.y

    def move(self, screen):
        "Déplacer le carré sur l'écran"
        direction_x = randint(-1, 1)
        direction_y = randint(-1, 1)
        self.rect.x += direction_x * self.speed
        self.rect.y += direction_y * self.speed

        if self.rect.x + self.width > self.x:
            self.rect.x = self.x - self.width

        if self.rect.y + self.height > self.y:
            self.rect.y = self.y - self.height

        if self.rect.x < 0:
            self.rect.x = 0

        if self.rect.y < 0:
            self.rect.y = 0

        self.draw(screen)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
