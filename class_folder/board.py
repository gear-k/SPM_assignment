import string
import math
import shutil
from pynput import keyboard

LETTERS = string.ascii_letters

class Board:
    def __init__(self, cells):
        self.cells = cells
        self.start = 0
        self.end = 0

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

    def display(self, page):
        terminal_size = math.floor((shutil.get_terminal_size().columns-4)/4/26)*26
        if page == 1 and len(self.cells) > self.end:
            size = len(self.cells) - self.end
        elif page == -1 and self.start > 0:
            size = len(self.cells) - self.start + terminal_size
        else:
            size = len(self.cells) - self.start
        #
        if size > terminal_size:
            if terminal_size > 52:
                terminal_size = 2
            temp = terminal_size
        elif size > 52:
            temp = 52
        else:
            temp = size
        # print("temp", temp)
        # print("board-start", self.start)
        # print("board-end", self.end)
        # print("size", size)
        if page == 1 and len(self.cells) > self.end:
            start = self.end
            self.start = self.end
            self.end += temp
            # print("check start", self.start)
            # print("check end", self.end)
        elif page == -1 and self.start > 0:
            start = self.start - temp
            self.end = self.start
            self.start -= temp
        else:
            start = self.start
            self.end = self.start + temp

        header = ["    "] + [f'  {LETTERS[i]} ' for i in range(temp)]
        separator = "    +" + "---+" * temp

        print("".join(header))
        for i in range(len(self.cells)):
            print(separator)
            row = [f"{i+1:2}  "]
            for j in range(temp):
                row.append(f"| {self.cells[i][j+start]} ")
            row.append("|")
            print("".join(row))
        print(separator)

        return header, separator, temp, start

    def check_arrow(self):
        print("Arrow Left to move Left - Arrow Right to move Right - Esc to continue")
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        
    def on_press(self, key):
        if key == keyboard.Key.left:  # Listen for left key
            self.display(-1)
        elif key == keyboard.Key.right:  # Listen for right key
            self.display(1)
        elif key == keyboard.Key.esc:
            return False
        print("Arrow Left to move Left - Arrow Right to move Right - Any other key to continue")
        
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
# board = Board.create_board(20)
# board.cells[0][0] = "1"
# board.cells[19][19] = "a"
# board.display(0)
# board.display(1)
# board.display(-1)

# board.expand_board()
# board.display()
