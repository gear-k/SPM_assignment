import string

LETTERS = string.ascii_lowercase

class Board:
    def __init__(self, cells):
        self.cells = cells

    @staticmethod
    def create_board(size):
        cells = [[" " for _ in range(size)] for _ in range(size)]
        return cells

    def display(self):
        size = len(self.cells)
        header = ["   "] + [f" {LETTERS[i]} " for i in range(size)] + ["\n"]
        separator = "\n    " + "---+" * (size - 1) + "---"
        
        print("".join(header))
        for i in range(size):
            row = [f"{i+1:2}  "]
            for j in range(size):
                row.append(f" {self.cells[i][j]} |")
            row[-1] = f" {self.cells[i][-1]} "
            print("".join(row))
            if i < size - 1:
                print(separator)
