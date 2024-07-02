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

class Freeplay:
    def __init__(self, turn, score, lossStreak, board):
        self.turn = turn
        self.score = score
        self.lossStreak = lossStreak
        self.board = board
    
    @staticmethod
    def start_new_free_play_game():
        print("Starting new Free Play game...\n")
        board = Board.create_board(5)
        Freeplay(1, 0, 5, board).play_free_play_game()

    def build_option(self):
        print("Select the building to construct:")
        for idx, building in enumerate(BUILDINGS, start=1):
            print(f"{idx}. {building}")

        try:
            building_choice = int(input("Enter building option you want to construct: "))
            if 1 <= building_choice <= 5:
                building = Building(list(BUILDINGS.values())[building_choice - 1])
                self.board = building.build_building(self.board)

                if any(r in [0, len(self.board.cells)-1] or c in [0, len(self.board.cells[0])-1] for r, c in [(r, c) for r in range(len(self.board.cells)) for c in range(len(self.board.cells[0])) if self.board.cells[r][c] != " "]):
                    print("hihi")
                    self.board.expand_board()

                return self.board
            else:
                print("Invalid building choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")

    def play_free_play_game(self):
        while self.lossStreak < 20:
            print(f"Turn: {self.turn}")
            print(f"Turn: {self.lossStreak}")
            self.score = Score.calculate_score(self.board)
            print(f"Score: {self.score}")
            self.turn += 1

            self.board.display()

            choice = input("Enter your choice: 1 to build, 2 to demolish, 3 to save, 4 to end: ")
            if choice == '1':
                self.board = self.build_option()
            elif choice == '2' and not self.board.isEmpty():
                self.board = Building.demolish_building(self.board, BUILDINGS)
            elif choice == '3':
                External.save_game(self.board, self.turn, self.lossStreak, 'freeplay')
                self.turn -= 1
            elif choice == '4':
                break
            else:
                print("Invalid choice, please try again.")
                self.turn -= 1

            income, upkeep = Freeplay.calculate_upkeep(self.board)
            profit = income - upkeep
            
            print(f"Income: {income}, Upkeep: {upkeep}, Net profit: {profit}")

            if profit < 0:
                lossStreak += 1
            else:
                lossStreak = 0
            
        External.end_game(self.score)

    @staticmethod
    def calculate_upkeep(board):
        coins = 0
        upkeep = 0
        residential_clusters = []
        for r in range(len(board.cells)):
            for c in range(len(board.cells[0])):
                if board.cells[r][c] == 'R':
                    coins += 1
                    # Find cluster of residential buildings
                    if not any((r, c) in cluster for cluster in residential_clusters):
                        cluster = Freeplay.find_cluster(board, r, c, 'R')
                        residential_clusters.append(cluster)
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
                    if not board.isValid(r, c):
                        upkeep += 1
        upkeep += len(residential_clusters)
        return coins, upkeep

    @staticmethod
    def find_cluster(board, row, col, building_type):
        cluster = [(row, col)]
        to_check = [(row, col)]
        while to_check:
            r, c = to_check.pop()
            adjacent_positions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for rr, cc in adjacent_positions:
                if 0 <= rr < len(board.cells) and 0 <= cc < len(board.cells[0]) and board.cells[rr][cc] == building_type and (rr, cc) not in cluster:
                    cluster.append((rr, cc))
                    to_check.append((rr, cc))
        return cluster

# board = Board.create_board(5)
# Freeplay.start_new_free_play_game()