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
pygame.mixer.init()


screen_width = 800  # Hauteur de l'écran
screen_height = 600  # Largeur de l'écran

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the square !")


def ask_quit():
    "Demander au joueur s'il souhaite arrêter la partie"
    ask = messagebox.askquestion(
        "Arrêter la partie en cours ?", "Souhaitez-vous vraiment quitter la partie en cours ?")
    return ask


def update_time_left(duree, secondes, minutes):
    "Mettre à jour le temps restant"
    temps = pygame.time.get_ticks()
    duree -= temps
    secondes = duree / 1000
    print("secondes :", secondes)
    minutes = duree / 60000
    print("minutes :", minutes)
    return secondes, minutes


def convert_time_left(duree, sec, min):
    "Convertir le temps restant en minutes : secondes"
    temps_restant = update_time_left(duree, sec, min)
    for index, valeur in enumerate(temps_restant):
        print(f"Index : {index}, Valeur : {valeur}")
        global secondes
        secondes = temps_restant[0]
        global minutes
        minutes = temps_restant[1]
        secondes_par_minute = 60  # Nombre de secondes dans une minute
        if secondes < secondes_par_minute:
            minutes -= 1


def display_time_left():
    time_left_font = pygame.font.Font(None, 36)
    str_temps_restant = time_left_font.render(
        f"{minutes} : {secondes}", True, (255, 255, 255))

    screen.blit(str_temps_restant, (0, 80))


def game():
    "Démarrer une nouvelle partie"
    carre = Carre(screen_width, screen_height)
    pseudo = entrer_pseudo()
    creer_dossier()  # Créer un dossier au nom du joueur s'il n'existe pas encore
    fichier_score = creer_fichier_score()
    joueur = Joueur(pseudo=pseudo, fichier_score=fichier_score)

    GAME_OVER = pygame.USEREVENT + 1
    duree_partie = 1000 * 120  # Durée de la partie convertie en millisecondes
    secondes = duree_partie / 1000
    minutes = duree_partie / 60000
    secondes_par_min = secondes / 2  # Nombre de secondes dans une minute
    print(secondes_par_min)

    print(f"minutes : {minutes}, secondes : {secondes}")

    pygame.time.set_timer(GAME_OVER, duree_partie)

    chemin_musique = "musique/catch_the_square.mp3"
    pygame.mixer.music.load(chemin_musique)
    pygame.mixer.music.play(-1)

    pygame.display.flip()
    running = True  # Est-ce que le jeu est en cours d'exécution ?
    while running:
        # print("Temps restant :", duree_partie / 1000)
        screen.fill((0, 0, 0))
       # update_time_left(duree_partie, secondes, minutes)
        convert_time_left(duree_partie, secondes, minutes)

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

        display_time_left()

        pygame.display.flip()


game()  # Lancer le jeu
