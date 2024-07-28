import random
from class_folder.board import Board
from class_folder.building import Building
from class_folder.external import External
from class_folder.score import Score

# Difficulty Settings
Difficulty = """
            *****************************
            *                           *
            *    Choose Difficulty:     *
            *                           *
            *    1. Easy (1)            *
            *                           *
            *    2. Hard (2)            *
            *                           *
            *****************************
"""

# Define the possible building types and their symbols
BUILDINGS = {
    "*": "Road",
    "O": "Park",
    "R": "Residential",
    "I": "Industry",
    "C": "Commercial",
}

class Freeplay:
    def __init__(self, difficulty, turn, score, lossStreak, board):
        self.mode = "Freeplay"
        self.difficulty = difficulty
        self.turn = turn
        self.score = score
        self.lossStreak = lossStreak
        self.board = board

    @staticmethod
    def start_new_free_play_game():
        # Starts a new Free Play game by initializing the board and game state
        try:
            print("Starting new Free Play game...\n")
            board = Board.create_board(5)
            print(Difficulty) # Display the difficulty menu
            difficulty = input("Choose difficulty: ").strip()
            if difficulty == '1':
                Freeplay("Easy", 1, 0, 0, board).play_free_play_game()
            elif difficulty == '2':
                Freeplay("Hard", 1, 0, 0, board).play_free_play_game()            
        except Exception as e:
            print(f"An error occurred while starting a new game: {e}")

    def build_option(self):
        # Allows the player to choose and place a building on the board
        print("-------------------------------------")
        print("Select building to construct:")
        for idx, building in enumerate(BUILDINGS.values(), start=1):
            print(f"{idx}. {building}")
        print("6. Cancel")
        while True:
            try:
                building_choice = input("\nEnter building option for construction: ").strip()
                building_choice = int(building_choice.replace(" ", ""))  # Remove spaces and convert to int
                if 1 <= building_choice <= len(BUILDINGS):
                    building = Building(list(BUILDINGS.values())[building_choice - 1])
                    self.board = building.build_building(self.board, self.mode, self)
                    # Check if any building is placed at the edge of the board and expand if necessary
                    if any(r in [0, len(self.board.cells)-1] or c in [0, len(self.board.cells[0])-1] for r, c in [(r, c) for r in range(len(self.board.cells)) for c in range(len(self.board.cells[0])) if self.board.cells[r][c] != " "]):
                        self.board.expand_board()
                    break
                elif building_choice == 6:  # Give the player the option to cancel the option
                    print("Build option canceled. Returning to previous menu.")
                    self.turn -= 1
                    break
                else:
                    print("Invalid building choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 5.")
            except Exception as e:
                print(f"An error occurred while selecting a building option: {e}")

    def play_free_play_game(self):
        # Main loop for the Free Play game where the player takes turns to build, demolish, save, or end the game
        try:
            while self.lossStreak < 20:
                print(f"Turn: {self.turn}")
                print(f"Loss Streak: {self.lossStreak}")
                self.score = Score.calculate_score(self.board, self.mode)
                print(f"Score: {self.score}")
                self.turn += 1

                self.board.display(0)
                self.board.check_arrow()

                choice = input("Enter your choice: 1 to build, 2 to demolish, 3 to save, 4 to end: ").strip()
                choice = choice.replace(" ", "")  # This feature allows the input to accept spacebars by auto removing them
                if choice == '1':
                    self.build_option()
                elif choice == '2' and not self.board.isEmpty():
                    self.board = Building.demolish_building(self.board, BUILDINGS, self, self.mode)
                elif choice == '3':
                    External.save_game(self.board, self.turn, self.lossStreak, 'freeplay')
                    self.turn -= 1
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Please try again.")
                    self.turn -= 1

                income, upkeep = Freeplay.calculate_upkeep(self.board)
                if self.difficulty == "Hard":
                    upkeep *= 2  # Corrected to actually double the upkeep in Hard mode
                profit = income - upkeep

                print(f"Income: {income}, Upkeep: {upkeep}, Net profit: {profit}")

                if profit < 0:
                    self.lossStreak += 1
                else:
                    self.lossStreak = 0

            External.end_game(self.score)
        except Exception as e:
            print(f"An error occurred during the game: {e}")

    @staticmethod
    def calculate_upkeep(board):
        income = 0
        upkeep = 0
        visited = set()

        for r in range(len(board.cells)):
            for c in range(len(board.cells[0])):
                if (r, c) not in visited:
                    if board.cells[r][c] == 'R':
                        income += 1
                        upkeep += 1
                    elif board.cells[r][c] == 'I':
                        income += 2
                        upkeep += 1
                        connected_buildings = board.find_connected_buildings(r, c)
                        income += sum(1 for rr, cc in connected_buildings if board.cells[rr][cc] == 'R')
                    elif board.cells[r][c] == 'C':
                        income += 3
                        upkeep += 2
                        connected_buildings = board.find_connected_buildings(r, c)
                        income += sum(1 for rr, cc in connected_buildings if board.cells[rr][cc] == 'R')
                    elif board.cells[r][c] == 'O':
                        upkeep += 1
                    elif board.cells[r][c] == '*':
                        upkeep += 1

                    visited.add((r, c))
                    visited.update(board.find_connected_buildings(r, c))

        return income, upkeep

    @staticmethod
    def find_cluster(board, row, col, building_type):
        cluster = [(row, col)]
        to_check = [(row, col)]
        while to_check:
            r, c = to_check.pop()
            adjacent_positions = [(r-1, c), (r+1, c), (r, col-1), (r, col+1)]
            for rr, cc in adjacent_positions:
                if 0 <= rr < len(board.cells) and 0 <= cc < len(board.cells[0]) and board.cells[rr][cc] == building_type and (rr, cc) not in cluster:
                    cluster.append((rr, cc))
                    to_check.append((rr, cc))
        return cluster

# Uncomment the following line to start a new Free Play game:
# Freeplay.start_new_free_play_game()
