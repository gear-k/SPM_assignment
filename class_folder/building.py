import string
import re

LETTERS = string.ascii_lowercase
BUILDINGS = {
    "*": "Road",
    "O": "Park",
    "R": "Residential",
    "I": "Industry",
    "C": "Commercial",
}

class Building:
    def __init__(self, building):
        self.building = building

    def build_building(self, board, mode):
        while True:
            try:
                position = input("Enter the position to place the building (e.g., A1): ")
                if position[1].isalpha():
                    col = LETTERS.index(position[0].lower()) * 26 + LETTERS.index(position[1].lower())
                    row = int(position[2:]) - 1
                else:
                    col = LETTERS.index(position[0].lower())
                    row = int(position[1:]) - 1
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
                    break
                else:
                    print("Invalid placement. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid row and column.")

        return board
    
    @staticmethod
    def demolish_building(board, BUILDINGS):
        while True:
            try:
                position = input("Enter the position of the building to demolish (e.g., A1): ")
                if position[1].isalpha():
                    col = LETTERS.index(position[0].lower()) * 26 + LETTERS.index(position[1].lower())
                    row = int(position[2:]) - 1
                else:
                    col = LETTERS.index(position[0].lower())
                    row = int(position[1:]) - 1
                if row < 0 or col < 0 or row >= len(board.cells) or col >= len(board.cells[0]):
                    raise IndexError()
                if board.cells[row][col] != " ":
                    building = BUILDINGS.get(board.cells[row][col], "Building")
                    board.cells[row][col] = " "
                    print(f"{building} removed at {position}")
                    break
                else:
                    print("No building at this place. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid row and column.")

        return board

# Example usage:
# from class_folder.board import Board
# board = Board.create_board(5)
# board.display()
# building1 = Building("Road")
# building1.build_building(board).display()
# Building.demolish_building(board, BUILDINGS).display()
