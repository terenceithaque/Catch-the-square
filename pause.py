# Mettre le jeu en pause
import pygame


pause = False  # Le jeu est-il en pause ?


def pause(keys):
    "Mettre le jeu en pause"
    if keys[pygame.K_SPACE]:
        if not pause:
            pause = True

        else:
            pause = False
