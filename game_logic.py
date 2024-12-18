import random

colors = []
secret_combination = []
user_combination = []
length = 4
attempts = 10
message_end_game = ""

def generate_secret_combination(length):
    """choices = va nous permettre d'avoir des entiers aléatoires qui peuvent se répeter"""
    secret_combination = random.choices(range(1, 7), k = length)
    return secret_combination


def input_user_combination(length):
    """Demande à l'utilisateur de proposer une combinaison valide."""
    user_combination = []
    while len(user_combination) < length:
        try:
            input_color = int(input("Entrez une couleur (chiffres entre 1 et 6) : "))
            if 1 <= input_color <= 6:
                user_combination.append(input_color)
            else:
                print("Erreur : La couleur doit être un chiffre entre 1 et 6 ")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier ")
    return user_combination


def verify_input_user(secret_combination, user_combination):

    correct_positions = 0
    correct_colors = 0

    for i in range(len(secret_combination)):
        if user_combination[i] == secret_combination[i]:
            correct_positions += 1
            user_combination[i] = None

    for i in range(len(secret_combination)):
        if user_combination[i] is not None:
            for j in range(len(secret_combination)):
                if user_combination[i] == secret_combination[j]:
                    correct_colors += 1
                    secret_combination[j] = None
                    break 
    if correct_positions == length:
        message_end_game = "Bravo, vous êtes un boss"
    elif correct_positions < length:
        message_end_game = ("encore un effort vous avez " + str(correct_positions) + " positions correctes et " + str(correct_colors) + " bonnes couleurs")
    print (message_end_game)
    return correct_positions, correct_colors




"""Boucle du jeu"""

secret_combination = [2, 1, 5, 3]
user_combination = [2, 5, 1, 3]

l = verify_input_user(secret_combination, user_combination)







