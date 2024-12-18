import random

colors = []
secret_combination = []
user_combination = []
length = 4
attempts = 10
message_end_game = ""

def generate_secret_combination(length):
    """choices = va nous permettre d'avoir des entiers aléatoires qui peuvent se répeter"""
    secret_combination = random.choices(range(2, 6), k = length)
    return secret_combination


def input_user_combination(length):
    """Demande à l'utilisateur de proposer une combinaison valide."""
    user_combination = []
    while len(user_combination) < length:
        try:
            input_color = int(input("Entrez une couleur (chiffres entre 2 et 6) : "))
            if 2 <= input_color <= 6:
                user_combination.append(input_color)
            else:
                print("Erreur : La couleur doit être un chiffre entre 2 et 6 ")
        except ValueError:
            print("Erreur : Veuillez entrer un nombre entier ")
    return user_combination

def verify_input_user(secret_combination, user_combination):
    for i in ran
    if secret_combination.index == user_combination.index 



"""Boucle du jeu

secret_combination = generate_secret_combination(length)
user_combination = input_user_combination(length)

print (message_end_game)
"""





