# Residential (R)
# Industry (I)
# Commercial (C)
# Park (O)
# Road (*)

import json
import random
import string
from class_folder.board import Board

BUILDINGS = ["Residential", "Industry", "Commercial", "Park", "Road"]
LETTERS = string.ascii_lowercase

def load_high_scores():
    try:
        with open('high_scores.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_high_scores(high_scores):
    with open('high_scores.json', 'w') as file:
        json.dump(high_scores, file)

def display_main_menu():
    high_scores = load_high_scores()
    while True:
        print("Welcome to Ngee Ann City Building Game!")
        print("1. Start New Arcade Game")
        print("2. Start New Free Play Game")
        print("3. Load Saved Game")
        print("4. Display High Scores")
        print("5. Exit Game")
        choice = input("Enter your choice: ")
        if choice == '1':
            start_new_arcade_game()
        elif choice == '2':
            start_new_free_play_game()
        elif choice == '3':
            load_saved_game()
        elif choice == '4':
            display_high_scores(high_scores)
        elif choice == '5':
            exit_game()
            break
        else:
            print("Invalid choice, please try again.")

def start_new_arcade_game():
    print("Starting new Arcade game...")
    # Placeholder for Arcade game initialization and play logic
    play_arcade_game(game_state=None)

def start_new_free_play_game():
    print("Starting new Free Play game...")
    # Placeholder for Free Play game initialization and play logic
    play_free_play_game()

def load_saved_game():
    filename = input("Enter the filename of the saved game: ")
    try:
        with open(filename, 'r') as file:
            game_state = json.load(file)
            if game_state['mode'] == 'arcade':
                play_arcade_game(game_state)
            elif game_state['mode'] == 'free_play':
                play_free_play_game(game_state)
    except FileNotFoundError:
        print("Saved game not found. Please try again.")

def display_high_scores(high_scores):
    print("High Scores:")
    for index, score in enumerate(sorted(high_scores, key=lambda x: x['score'], reverse=True)[:10]):
        print(f"{index + 1}. {score['name']} - {score['score']}")

def exit_game():
    print("Exiting the game. Goodbye!")

def play_arcade_game(game_state):
    print("Arcade game logic goes here.")
    # Placeholder for Arcade game play logic

    if game_state != None:
        board = game_state
    else:
        board = Board.create_board(20)

    turn = 0
    coin = 16
    score = 0
    while coin > 0:
        print("Turn : ", turn)
        turn += 1
        print("Score: ", score)

        building1 = random.randint(0, 4)
        building2 = random.randint(0, 4)
        print("Building choices\n - " + BUILDINGS[building1] + "\n - " + BUILDINGS[building2] + "\n")

        for row in board:
            print(" ".join(row))

        print("\nWhat would u like to do?")
        print("1. Build a " + BUILDINGS[building1])
        print("2. Build a " + BUILDINGS[building2])
        print("3. Demolish a Building")
        print("4. Saved Game")
        print("5. End Game")
        choice = input("Enter your choice: ")
        if choice == '1':
            continue
        elif choice == '2':
            continue
        elif choice == '3':
            continue
        elif choice == '4':
            continue
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")


def play_free_play_game(game_state=None):
    print("Free Play game logic goes here.")
    # Placeholder for Free Play game play logic

def countPoints():
    return

if __name__ == '__main__':
    display_main_menu()
