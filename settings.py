# Paramètres de la partie

square_speed = 2  # Vitesse intiale du carré


def change_square_speed(item, index):
    "Changer la vitesse du carré"
    print("Item sélectionné :", item)
    if item == "((Lente, 0) 0)":
        square_speed -= 1  # Augmenter la vitesse du carré
        print("Vitesse du carré :", square_speed)

    elif item == "Rapide":
        square_speed += 2
        print("Vitesse du carré :", square_speed)


def get_square_speed():
    "Obtenir la vitesse du carré"
    return square_speed
