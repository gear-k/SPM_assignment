import random
from board import Board
from building import Building
from external import External

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
        Arcade.play_arcade_game(board, 16)

    @staticmethod
    def build_option(board, building1, building2):
        print("Select the building to construct:")
        print(f"1. {building1}\n2. {building2}")

        building_choice = int(input("Enter building option you want to construct: "))
        if building_choice == '1':
            return building1.build_building(board)
        elif building_choice == '2':
            return building2.build_building(board)

    @staticmethod
    def play_arcade_game(board, coins):
        score = 0
        turn = 0

        while coins > 0 and any(" " in row for row in board.cells):
            print(f"Turn: {turn}")
            turn += 1

            board.display()

            building1, building2 = Building(random.sample(BUILDINGS.values)), Building(random.sample(BUILDINGS.values))
            print(f"Building choices: 1. {building1} 2. {building2}")

            choice = input("Enter your choice (1 or 2) to build, 3 to demolish, 4 to save, 5 to end: ")
            if choice == '1':
                board = Arcade.build_option(board, building1, building2)
                coins -= 1
            elif choice == '2' and not board.isEmpty:
                board = Building.demolish_building(board, BUILDINGS)
                coins -= 1
            elif choice == '3':
                External.save_game(board, turn, coins, 'arcade')
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

            # income, upkeep = calculate_upkeep(board)
            # coins += income - upkeep
            # score = calculate_score(board)
            
            # print(f"Income: {income}, Upkeep: {upkeep}, Net coins: {coins}")
            # print(f"Score: {score}")

        External.end_game(score)