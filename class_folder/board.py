import string
import math

LETTERS = string.ascii_lowercase

class Board:
    def __init__(self, cells):
        self.cells = cells

    @staticmethod
    def create_board(size):
        cells = [[" " for _ in range(size)] for _ in range(size)]
        return Board(cells)
    
    def expand_board(self):
        size = len(self.cells) + 10
        new_board = [[" " for _ in range(size)] for _ in range(size)]
        for r in range(len(self.cells)):
            for c in range(len(self.cells[0])):
                new_board[r + 5][c + 5] = self.cells[r][c]
        self.cells = new_board
        print("City expanded!")

    def display(self):
        size = len(self.cells)
        header1 = ["    "] + [f'  {LETTERS[i % 26]} ' for i in range(size)]
        header2 = ["    "] + [f' ({LETTERS[i // 26]}){" "*25*4}' for i in range(size) if i % 26 == 0]
        separator = "    +" + "---+" * size

        print("".join(header2))
        print("".join(header1))
        for i in range(size):
            print(separator)
            row = [f"{i+1:2}  "]
            for j in range(size):
                row.append(f"| {self.cells[i][j]} ")
            row.append("|")
            print("".join(row))
        print(separator)

    def isEmpty(self):
        return all(all(cell == " " for cell in row) for row in self.cells)

    def isValid(self, row, col):
        if 0 <= row < len(self.cells) and 0 <= col < len(self.cells) and self.cells[row][col] == " ":
            adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            for r, c in adjacent_positions:
                if 0 <= r < len(self.cells) and 0 <= c < len(self.cells[0]) and self.cells[r][c] != " ":
                    return True
        return False

# Example usage:
# board = Board.create_board(53)
# board.display()
# board.expand_board()
# board.display()
