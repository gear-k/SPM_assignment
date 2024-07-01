import string
from board import Board

LETTERS = string.ascii_lowercase

class Building:
    def __init__(self, building):
        self.building = building

    def build_building(self, board):
        while True:
            try:
                postion = input("Enter the postion to place the building(e.g. A1): ")
                col = LETTERS.index(postion[0].lower())
                row = int(postion[1]) - 1
                if row < 0 or col < 0:
                    raise IndexError()
                if board.isEmpty or board.isValid(row, col):
                    if self.building == "Road":
                        board.cells[row][col] = "*"
                    elif self.building == "Park":
                        board.cells[row][col] = "O"
                    else:
                        board.cells[row][col] = self.building[0]
                    print(f"{self.building} placed at {postion}")
                    break
                else:
                    print("Invalid placement. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column.")

        return board
    
    @staticmethod
    def demolish_building(board, BUILDINGS):
        while True:
            try:
                postion = input("Enter the postion of building to demolish(e.g. A1): ")
                col = LETTERS.index(postion[0].lower())
                row = int(postion[1]) - 1
                if row < 0 or col < 0:
                    raise IndexError()
                if board.cells[row][col] != " ":
                    building = BUILDINGS[board.cells[row][col]]
                    board.cells[row][col] = " "
                    print(f"{building} removed at {postion}")
                    break
                else:
                    print("No building at this place. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid row and column.")

        return board


BUILDINGS = {
    "*": "Road",
    "O": "Park",
    "R": "Residential",
    "I": "Industry",
    "C": "Commercial",
}


board = Board.create_board(5)
board = Board([['*', 'C'], ['I', 'O']])
# board.display()
print(type(board.cells))

building1, building2 = Building("Road"), Building("Industry")
# print(building1.building, building2.building)
# print(board.isValid(0, 0))

# building1.build_building(board).display()
# Building.demolish_building(board, BUILDINGS).display()


