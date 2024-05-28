import json

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
    play_arcade_game()

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

def play_arcade_game(game_state=None):
    print("Arcade game logic goes here.")
    # Placeholder for Arcade game play logic

def play_free_play_game(game_state=None):
    print("Free Play game logic goes here.")
    # Placeholder for Free Play game play logic

if __name__ == '__main__':
    display_main_menu()
