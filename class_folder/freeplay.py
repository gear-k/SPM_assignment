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

class Freeplay:
    def __init__(self, turn, score, coins, board):
        self.turn = turn
        self.score = score
        self.coins = coins
        self.board = board
    
    @staticmethod
    def start_new_free_play_game():
        print("Starting new Free Play game...\n")
        board = Board.create_board(5)
        Freeplay.play_free_play_game(board)

    @staticmethod
    def build_option(board):
        print("Select the building to construct:")
        for idx, building in enumerate(BUILDINGS, start=1):
            print(f"{idx}. {building}")

        building_choice = int(input("Enter building option you want to construct: "))
        try:
            building_choice = int(input("Enter the number of the building you want to construct: "))
            if 1 <= building_choice <= 5:
                building = Building(BUILDINGS[building_choice - 1])
                board = building.build_building(board)

                if any(r in [0, len(board.cells)-1] or c in [0, len(board.cells[0])-1] for r, c in [(r, c) for r in range(len(board.cells)) for c in range(len(board.cells[0])) if board.cells[r][c] != " "]):
                    board.expand_board()

                return board
            else:
                print("Invalid building choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    @staticmethod
    def play_free_play_game(board):
        score = 0
        turn = 0
        loss_streak = 0

        while loss_streak < 20:
            print(f"Turn: {turn}")
            turn += 1

            board.display()

            choice = input("Enter your choice: 1 to build, 2 to demolish, 3 to save, 4 to end: ")
            if choice == '1':
                board = Freeplay.build_option(board)
            elif choice == '2' and not board.isEmpty:
                board = Building.demolish_building(board, BUILDINGS)
            elif choice == '3':
                External.save_game(board, turn, loss_streak, 'freeplay')
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")

            # income, upkeep = calculate_upkeep(board)
            # coins += income - upkeep
            # score = calculate_score(board)
            
            # print(f"Income: {income}, Upkeep: {upkeep}, Net coins: {coins}")
            # print(f"Score: {score}")

            # if coins < 0:
            #     loss_streak += 1
            # else:
            #     loss_streak = 0
            
        External.end_game(score)