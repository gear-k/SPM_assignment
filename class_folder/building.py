import string
import re  # Import regex module for validation

LETTERS = string.ascii_lowercase
BUILDINGS = {
    "*": "Road",
    "O": "Park",
    "R": "Residential",
    "I": "Industry",
    "C": "Commercial",
}

class Board:
    def __init__(self, rows, cols):
        self.cells = [[" " for _ in range(cols)] for _ in range(rows)]

    @staticmethod
    def create_board(size):
        return Board(size, size)

    def display(self):
        for row in self.cells:
            print(" ".join(row))

    def isEmpty(self):
        return all(cell == " " for row in self.cells for cell in row)

    def isValid(self, row, col):
        return self.cells[row][col] == " "

class Building:
    def __init__(self, building):
        self.building = building

    def build_building(self, board, mode, player):
        while True:
            try:
                position = input("Enter the position to place the building (e.g., A1): ")
                position = position.replace(" ", "")  # This feature allows the input to accept spacebars by auto removing them
                if not re.match(r'^[A-Z][0-9]+$', position):
                    print("Invalid input. Please enter a valid coordinate like A1.")
                    continue

                # Parse the position into row and col
                row = ord(position[0].upper()) - ord('A')
                col = int(position[1:]) - 1

                if row < 0 or col < 0 or row >= len(board.cells) or col >= len(board.cells[0]):
                    raise IndexError()
                if board.isEmpty() or board.isValid(row, col) or mode == "Freeplay":
                    if self.building == "Road":
                        board.cells[row][col] = "*"
                    elif self.building == "Park":
                        board.cells[row][col] = "O"
                    else:
                        board.cells[row][col] = self.building[0]
                    print(f"{self.building} placed at {position}")
                    if mode != "Freeplay":
                        player.coins -= 1
                    break
                else:
                    print("Invalid placement. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid row and column.")

        return board
    
    @staticmethod
    def demolish_building(board, BUILDINGS, player, mode):
        total_buildings = sum(1 for row in board.cells for cell in row if cell != " ")

        if total_buildings <= 1:
            print("Cannot demolish the only building on the board.")
            return board

        while True:
            try:
                position = input("Enter the position of the building to demolish (e.g., A1): ")
                position = position.replace(" ", "")  # This feature allows the input to accept spacebars by auto removing them
                if not re.match(r'^[A-Z][0-9]+$', position):
                    print("Invalid input. Please enter a valid coordinate like A1.")
                    continue

                # Parse the position into row and col
                row = ord(position[0].upper()) - ord('A')
                col = int(position[1:]) - 1

                if row < 0 or col < 0 or row >= len(board.cells) or col >= len(board.cells[0]):
                    raise IndexError()
                if board.cells[row][col] != " ":
                    building = BUILDINGS.get(board.cells[row][col], "Building")
                    board.cells[row][col] = " "
                    print(f"{building} removed at {position}")
                    if mode != "Freeplay":
                        player.coins -= 1
                    break
                else:
                    print("No building at this place. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid row and column.")
                if mode != "Freeplay":
                    player.coins += 1  # Refund the coin for invalid demolition

        return board
