import string
import math
import shutil
import sys
from pynput import keyboard
from colorama import Fore, Style, init

init(autoreset=True)

LETTERS = string.ascii_letters

class Board:
    def __init__(self, cells):
        self.cells = cells
        self.start = 0
        self.end = min(len(cells), self.get_terminal_width())  # Initialize `end` correctly

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

    def get_terminal_width(self):
        # Get the terminal width adjusted for the board display
        terminal_columns = shutil.get_terminal_size().columns
        # Calculate the number of cells that fit in the terminal width
        return math.floor((terminal_columns - 4) / 4 / 26) * 26
    
    def display(self, page):
        size = len(self.cells)
        terminal_size = self.get_terminal_width()
        
        if page == 1 and len(self.cells) > self.end:
            size = len(self.cells) - self.end
        elif page == -1 and self.start > 0:
            size = len(self.cells) - self.start + terminal_size
        else:
            size = len(self.cells) - self.start

        if size > terminal_size:
            if terminal_size > 52:
                terminal_size = 52
            temp = terminal_size
        elif size > 52:
            temp = 52
        else:
            temp = size

        if page == 1 and self.end < size:
            if size - self.end < 5:
                self.start += size - self.end
            else:
                self.start += 5

        if page == 1 and len(self.cells) > self.end:
            start = self.end
            self.start = self.end
            self.end += temp
        elif page == -1 and self.start > 0:
            if self.start < 5:
                self.start = 0
            else:
                self.start -= 5
        elif page == 0:
            self.start = 0
            self.end = self.start + temp
        else:
            return

        header = ["    "] + [f'  {LETTERS[i]} ' for i in range(temp)]
        separator = "    +" + "---+" * temp

        print("".join(header))
        for i in range(size):
            print(separator)
            row = [f"{i+1:2}  "]
            for j in range(temp):
                cell = self.cells[i][j+self.start]
                if cell.isdigit():
                    color = Fore.BLUE  # Blue for digits
                elif cell.isalpha():
                    color = Fore.GREEN  # Green for letters
                else:
                    color = Style.RESET_ALL
                row.append(f"| {color}{cell}{Style.RESET_ALL} ")
            row.append("|")
            print("".join(row))
        print(separator)

    def check_arrow(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()
        
    def on_press(self, key):
        if key == keyboard.Key.left:  # Listen for left key
            self.display(-1)
        elif key == keyboard.Key.right:  # Listen for right key
            self.display(1)
        else:
            return False
        
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
board = Board.create_board(20)
# board.cells[0][0] = "1"
# board.cells[19][19] = "a"
board.display(0)
# board.display(1)
# board.display(-1)

# board.expand_board()
# board.display()
