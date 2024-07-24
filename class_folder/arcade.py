import random
from class_folder.board import Board
from class_folder.building import Building
from class_folder.external import External
from class_folder.score import Score

# Define the possible building types and their symbols
BUILDINGS = {
    "*": "Road",
    "O": "Park",
    "R": "Residential",
    "I": "Industry",
    "C": "Commercial",
}

class Arcade:
    def __init__(self, turn, score, coins, board):
        self.mode = "Arcade"
        self.turn = turn
        self.score = score
        self.coins = coins
        self.board = board
    
    @staticmethod
    def start_new_arcade_game():
        try:
            print("Starting new Arcade game...\n")
            board = Board.create_board(20)
            Arcade(1, 0, 16, board).play_arcade_game()
        except Exception as e:
            print(f"An error occurred while starting a new arcade game: {e}")

    def build_option(self, building1, building2):
        print("-------------------------------------")
        print("Select the building to construct:")
        print(f"1. {building1.building}\n2. {building2.building}\n")

        while True:
            try:
                building_choice = input("Enter building option for construction: ").strip()
                building_choice = int(building_choice.replace(" ", ""))  # Remove spaces and convert to int
                if building_choice == 1:
                    self.board = building1.build_building(self.board, self.mode, self)
                elif building_choice == 2:
                    self.board = building2.build_building(self.board, self.mode, self)
                elif building_choice == 3:  # For when the user wants to reconsider their move
                    print("Build option canceled. Returning to previous menu.")
                    self.turn -= 1  # Only increment turn if a building is constructed
                    self.coins += 1  # Give back the coins spent
                    return False  # Indicate that the action was canceled
                else:
                    print("Invalid building choice. Please try again.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter 1, 2 or 3.")
            except Exception as e:
                print(f"An error occurred while building: {e}")
        
    def play_arcade_game(self):
        try:
            if self.board is None:
                raise ValueError("Board must be initialized before starting the game.")
            if self.board.cells is None:
                raise ValueError("Board must have cells initialized before starting the game.")
            
            while self.coins > 0 and any(" " in row for row in self.board.cells):
                print(f"\nTurn: {self.turn}")
                print(f"Coins: {self.coins}")
                self.score = Score.calculate_score(self.board)
                print(f"Score: {self.score}")
                self.turn += 1

                self.board.display(0)

                r1, r2 = random.sample(list(BUILDINGS.values()), 2)
                building1, building2 = Building(r1), Building(r2)
                print(f"Building choices: {building1.building}, {building2.building}")

                choice = input("Enter 1 to build, 2 to demolish, 3 to save, 4 to end: ")
                choice = choice.replace(" ", "")  # This feature allows the input to accept spacebars by auto removing them
                if choice == '1':
                    self.build_option(building1, building2)
                    self.coins -= 1
                elif choice == '2' and not self.board.isEmpty():
                    self.board = Building.demolish_building(self.board, BUILDINGS, self, self.mode)
                    self.coins -= 1
                elif choice == '3':
                    External.save_game(self.board, self.turn, self.coins, 'arcade')
                    self.turn -= 1
                elif choice == '4':
                    break
                else:
                    print("Invalid choice, please try again.")
                    self.turn -= 1

                self.calculate_upkeep()

            External.end_game(self.score)
        except Exception as e:
            print(f"An error occurred while playing the arcade game: {e}")

    def calculate_upkeep(self):
        for r in range(len(self.board.cells)):
            for c in range(len(self.board.cells[0])):
                if self.board.cells[r][c] == 'I' or self.board.cells[r][c] == 'C':
                    adjacent_positions = [(r-1, c), (r+1, c), (r, col-1), (r, col+1)]
                    for rr, cc in adjacent_positions:
                        if 0 <= rr < len(self.board.cells) and 0 <= cc < len(self.board.cells[0]) and self.board.cells[rr][cc] == "R":
                            self.coins += 1

# To start a new arcade game, you can uncomment the following line:
# Arcade.start_new_arcade_game()
