import json
import os

class External:
    @staticmethod
    def save_game(board, turn, spec, mode):
        os.makedirs('storage', exist_ok=True)
        while True:
            filename = input("Enter the filename to save the game: ")
            if not os.path.isfile("storage/" + filename):
                break
            print("File name already in use. Please try again.")

        game_state = {
            'mode': mode,
            'board': board.cells,
            'turn': turn,
            'spec': spec
        }
        with open("storage/" + filename, 'w') as file:
            json.dump(game_state, file)
        print(f"Game saved as {filename}")

    @staticmethod
    def load_saved_game():
        filename = input("Enter the filename of the saved game: ")
        try:
            with open("storage/" + filename, 'r') as file:
                game_state = json.load(file)
                return game_state
        except FileNotFoundError:
            print("Saved game not found. Please try again.")
        except json.JSONDecodeError:
            print("Failed to decode saved game. The file might be corrupted.")
        return None

    @staticmethod
    def load_high_scores():
        try:
            with open('storage/high_scores.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("High scores file not found. Creating a new one.")
            return []
        except json.JSONDecodeError:
            print("Failed to decode high scores. The file might be corrupted.")
            return []

    @staticmethod
    def display_high_scores(high_scores):
        print("High Scores:")
        for index, score in enumerate(high_scores[:10]):
            print(f"{index + 1}. {score['name']} - {score['score']}")

    @staticmethod
    def end_game(score):
        print("Game over!")
        print(f"Final Score: {score}")

        name = input("Enter your name for the high score: ")
        high_scores = External.load_high_scores()
        high_scores.append({'name': name, 'score': score, 'track': len(high_scores)})
        high_scores.sort(key=lambda x: (x['score'], x['track']), reverse=True)

        os.makedirs('storage', exist_ok=True)
        with open('storage/high_scores.json', 'w') as file:
            json.dump(high_scores, file)

        External.display_high_scores(high_scores)
