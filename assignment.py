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
            high_scores = load_high_scores()
            display_high_scores(high_scores)
        elif choice == '5':
            exit_game()
            break
        else:
            print("Invalid choice, please try again.")

def start_new_arcade_game():
    print("Starting new Arcade game...")
    board = Board(Board.create_board(20))
    play_arcade_game(board, 16)

def start_new_free_play_game():
    print("Starting new Free Play game...")
    board = Board(Board.create_board(5))
    play_free_play_game(board)

def load_saved_game():
    filename = input("Enter the filename of the saved game: ")
    try:
        with open(filename, 'r') as file:
            game_state = json.load(file)
            if game_state['mode'] == 'arcade':
                play_arcade_game(Board(game_state['board']), game_state['coins'])
            elif game_state['mode'] == 'free_play':
                play_free_play_game(Board(game_state['board']))
    except FileNotFoundError:
        print("Saved game not found. Please try again.")

def display_high_scores(high_scores):
    print("High Scores:")
    for index, score in enumerate(sorted(high_scores, key=lambda x: x['score'], reverse=True)[:10]):
        print(f"{index + 1}. {score['name']} - {score['score']}")

def exit_game():
    print("Exiting the game. Goodbye!")

def is_valid_placement(board, row, col, first_turn):
    if board.cells[row][col] != " ":
        return False
    if first_turn:
        return True
    adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    for r, c in adjacent_positions:
        if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]) and board.cells[r][c] != " ":
            return True
    return False

def place_building(board, building, row, col):
    if building == "Road":
        board.cells[row][col] = "*"
    else:
        board.cells[row][col] = building[0]
    return board

def calculate_score(board):
    score = 0
    for r in range(len(board.cells)):
        for c in range(len(board.cells[0])):
            if board.cells[r][c] == 'R':
                score += calculate_residential_score(board, r, c)
            elif board.cells[r][c] == 'I':
                score += calculate_industry_score(board, r, c)
            elif board.cells[r][c] == 'C':
                score += calculate_commercial_score(board, r, c)
            elif board.cells[r][c] == 'O':
                score += calculate_park_score(board, r, c)
            elif board.cells[r][c] == '*':
                score += calculate_road_score(board, r, c)
    return score

def calculate_residential_score(board, row, col):
    score = 0
    adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    for r, c in adjacent_positions:
        if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]):
            if board.cells[r][c] == 'R' or board.cells[r][c] == 'C':
                score += 1
            elif board.cells[r][c] == 'O':
                score += 2
            elif board.cells[r][c] == 'I':
                score += 1
    return score

def calculate_industry_score(board, row, col):
    return sum(1 for r in range(len(board.cells)) for c in range(len(board.cells[0])) if board.cells[r][c] == 'I')

def calculate_commercial_score(board, row, col):
    score = 0
    adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    for r, c in adjacent_positions:
        if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]) and board.cells[r][c] == 'C':
            score += 1
    return score

def calculate_park_score(board, row, col):
    score = 0
    adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    for r, c in adjacent_positions:
        if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]) and board.cells[r][c] == 'O':
            score += 1
    return score

def calculate_road_score(board, row, col):
    score = 0
    for c in range(len(board.cells[0])):
        if board.cells[row][c] == '*':
            score += 1
    return score

def build_building(board, building, coins, first_turn):
    if coins <= 0:
        print("No more coins left.")
        return board, coins

    possible_positions = []
    for r in range(len(board.cells)):
        for c in range(len(board.cells[0])):
            if board.cells[r][c] == " " and (first_turn or is_valid_placement(board, r, c, first_turn)):
                possible_positions.append((r, c))

    if not possible_positions:
        print("No valid positions to place the building.")
        return board, coins

    print(f"Possible positions to place {building}:")
    for pos in possible_positions:
        print(f"Row {pos[0] + 1}, Column {LETTERS[pos[1]].upper()}")

    row = int(input("Enter the row to place the building: ")) - 1
    col = LETTERS.index(input("Enter the column to place the building: ").lower())

    if (row, col) in possible_positions:
        board = place_building(board, building, row, col)
        coins -= 1
        print(f"{building} placed at {row+1}, {LETTERS[col].upper()}")
    else:
        print("Invalid placement. Try again.")

    return board, coins

def play_arcade_game(board, coins):
    score = 0
    turn = 0
    first_turn = True

    while coins > 0:
        print(f"Turn: {turn}")
        turn += 1
        print(f"Coins: {coins}")
        print(f"Score: {score}")

        # Select two different random buildings
        building1, building2 = random.sample(BUILDINGS, 2)
        print(f"Building choices: 1. {building1} 2. {building2}")
        
        board.display()

        choice = input("Enter your choice (1 or 2) to build, 3 to demolish, 4 to save, 5 to end: ")

        if choice == '1':
            board, coins = build_building(board, building1, coins, first_turn)
        elif choice == '2':
            board, coins = build_building(board, building2, coins, first_turn)
        elif choice == '3':
            print("Demolish functionality not implemented yet.")
        elif choice == '4':
            print("Save functionality not implemented yet.")
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")

        first_turn = False
        score = calculate_score(board)

    print("Game over!")
    print(f"Final Score: {score}")

    # Save the high score
    name = input("Enter your name for the high score: ")
    high_scores = load_high_scores()
    high_scores.append({'name': name, 'score': score})
    save_high_scores(high_scores)

def expand_board(board):
    size = len(board.cells) + 10
    new_board = [[" " for _ in range(size)] for _ in range(size)]
    for r in range(len(board.cells)):
        for c in range(len(board.cells[0])):
            new_board[r + 5][c + 5] = board.cells[r][c]
    board.cells = new_board
    print("City expanded!")

def calculate_upkeep(board):
    coins = 0
    upkeep = 0
    for r in range(len(board.cells)):
        for c in range(len(board.cells[0])):
            if board.cells[r][c] == 'R':
                coins += 1
                if (r > 0 and board.cells[r-1][c] != 'R') or \
                   (r < len(board.cells) - 1 and board.cells[r+1][c] != 'R') or \
                   (c > 0 and board.cells[r][c-1] != 'R') or \
                   (c < len(board.cells[0]) - 1 and board.cells[r][c+1] != 'R'):
                    upkeep += 1
            elif board.cells[r][c] == 'I':
                coins += 2
                upkeep += 1
            elif board.cells[r][c] == 'C':
                coins += 3
                upkeep += 2
            elif board.cells[r][c] == 'O':
                upkeep += 1
            elif board.cells[r][c] == '*':
                if not is_valid_placement(board, r, c, False):
                    upkeep += 1
    return coins, upkeep

def play_free_play_game(board):
    coins = 100  # Starting with a large number of coins to simulate free play
    turn = 0
    first_turn = True

    while True:
        print(f"Turn: {turn}")
        turn += 1
        print(f"Coins: {coins}")

        board.display()

        choice = input("Enter your choice: 1 to build, 2 to demolish, 3 to save, 4 to end: ")

        if choice == '1':
            print("Select the building to construct:")
            for idx, building in enumerate(BUILDINGS, start=1):
                print(f"{idx}. {building}")
            building_choice = int(input("Enter the number of the building you want to construct: "))
            if 1 <= building_choice <= 5:
                building = BUILDINGS[building_choice - 1]
                board, coins = build_building(board, building, coins, first_turn)
                first_turn = False
                if any(r in [0, len(board.cells)-1] or c in [0, len(board.cells[0])-1] for r, c in [(r, c) for r in range(len(board.cells)) for c in range(len(board.cells[0])) if board.cells[r][c] != " "]):
                    expand_board(board)
            else:
                print("Invalid building choice. Please try again.")
        elif choice == '2':
            print("Demolish functionality not implemented yet.")
        elif choice == '3':
            print("Save functionality not implemented yet.")
        elif choice == '4':
            break
        else:
            print("Invalid choice, please try again.")

        income, upkeep = calculate_upkeep(board)
        coins += income - upkeep
        print(f"Income: {income}, Upkeep: {upkeep}, Net coins: {coins}")

    print("Game over!")

def countPoints():
    return

if __name__ == '__main__':
    display_main_menu()
