import random
from class_folder.board import Board
from class_folder.building import Building
from class_folder.external import External
from class_folder.score import Score

BUILDINGS = {
    "*": "Road",
    "O": "Park",
    "R": "Residential",
    "I": "Industry",
    "C": "Commercial",
}

class Arcade:
    def __init__(self, turn, score, coins, board):
        self.turn = turn
        self.score = score
        self.coins = coins
        self.board = board
    
    @staticmethod
    def start_new_arcade_game():
        print("Starting new Arcade game...\n")
        board = Board.create_board(20)
        Arcade(1, 0, 16, board).play_arcade_game()

    def build_option(self, building1, building2):
        print("Select the building to construct:")
        print(f"1. {building1.building}\n2. {building2.building}")

        try:
            building_choice = int(input("Enter building option you want to construct: "))
            if building_choice == 1:
                return building1.build_building(self.board)
            elif building_choice == 1:
                return building2.build_building(self.board)
            else:
                print("Invalid building choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    def play_arcade_game(self):
        while self.coins > 0 and any(" " in row for row in self.board.cells):
            print(f"Turn: {self.turn}")
            print(f"Turn: {self.coins}")
            self.score = Score.calculate_score(self.board)
            print(f"Score: {self.score}")
            self.turn += 1

            self.board.display()

            r1, r2 = random.sample(list(BUILDINGS.values()), 2)
            building1, building2 = Building(r1), Building(r2)
            print(f"Building choices: {building1.building}, {building2.building}")

            choice = input("Enter 1 to build, 2 to demolish, 3 to save, 4 to end: ")
            if choice == '1':
                self.board = self.build_option(building1, building2)
                self.coins -= 1
            elif choice == '2' and not self.board.isEmpty():
                self.board = Building.demolish_building(self.board, BUILDINGS)
                self.coins -= 1
            elif choice == '3':
                External.save_game(self.board, self.turn, self.coins, 'arcade')
                self.turn -= 1
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")
                self.turn -= 1

        External.end_game(self.score)

# board = Board.create_board(20)
# Arcade.start_new_arcade_game()