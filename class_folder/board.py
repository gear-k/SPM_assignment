import string

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
        header = ["    "] + [f"  {LETTERS[i]} " for i in range(size)]
        separator = "    +" + "---+" * (size - 1) + "---+"

        print("".join(header))
        for i in range(size):
            print(separator)
            row = [f"{i+1:2}  "]
            for j in range(size):
                row.append(f"| {self.cells[i][j]} ")
            row += "|"
            print("".join(row))
        print(separator)

    def isEmpty(self):
        if all(all(cell == " " for cell in row) for row in self.cells):
            return True

    def isValid(self, row, col):
        if self.cells[row][col] == " ":
            adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
            for r, c in adjacent_positions:
                if self.cells[r][c] != " ":
                    return True
        return False
