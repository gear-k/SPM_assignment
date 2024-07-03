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
            Freeplay("Easy", 1, 0, 0, board).play_free_play_game()
        except Exception as e:
            print(f"An error occurred while starting a new free play game: {e}")

    def build_option(self):
        # Allows the player to choose and place a building on the board
        print("Select the building to construct:")
        for idx, building in enumerate(BUILDINGS.values(), start=1):
            print(f"{idx}. {building}")
        while True:
            try:
                building_choice = int(input("Enter building option you want to construct: "))
                if 1 <= building_choice <= len(BUILDINGS):
                    building = Building(list(BUILDINGS.values())[building_choice - 1])
                    self.board = building.build_building(self.board, self.mode)
                    # Check if any building is placed at the edge of the board and expand if necessary
                    if any(r in [0, len(self.board.cells)-1] or c in [0, len(self.board.cells[0])-1] for r, c in [(r, c) for r in range(len(self.board.cells)) for c in range(len(self.board.cells[0])) if self.board.cells[r][c] != " "]):
                        self.board.expand_board()
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
                self.score = Score.calculate_score(self.board)
                print(f"Score: {self.score}")
                self.turn += 1
                
                self.board.display()

                choice = input("Enter your choice: 1 to build, 2 to demolish, 3 to save, 4 to end: ")
                if choice == '1':
                    self.build_option()
                elif choice == '2' and not self.board.isEmpty():
                    self.board = Building.demolish_building(self.board, BUILDINGS)
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
                    upkeep * 2
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
        # Calculates the income and upkeep of the current board state
        income = 0
        upkeep = 0
        residential_clusters = []
        road_clusters = []
        for r in range(len(board.cells)):
            for c in range(len(board.cells[0])):
                if board.cells[r][c] == 'R':
                    income += 1
                    # Find cluster of residential buildings
                    if not any((r, c) in cluster for cluster in residential_clusters):
                        cluster = Freeplay.find_cluster(board, r, c, 'R')
                        if len(cluster) > 1:
                            residential_clusters.append(cluster)
                        upkeep += 1
                elif board.cells[r][c] == 'I':
                    income += 2
                    upkeep += 1
                elif board.cells[r][c] == 'C':
                    income += 3
                    upkeep += 2
                elif board.cells[r][c] == 'O':
                    upkeep += 1
                elif board.cells[r][c] == '*':
                     # Find cluster of roads
                    if not any((r, c) in cluster for cluster in road_clusters):
                        cluster = Freeplay.find_cluster(board, r, c, '*')
                        if len(cluster) > 1:
                            road_clusters.append(cluster)
                        upkeep += 1
        return income, upkeep
    
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

# Uncomment the following line to start a new Free Play game:
# Freeplay.start_new_free_play_game()
