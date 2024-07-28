import string
import math
import shutil
from pynput import keyboard
from colorama import Fore, Style, init

init(autoreset=True)

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
        size = len(self.cells)
        terminal_size = math.floor((shutil.get_terminal_size().columns-4)/4/26)*26

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
                color = Style.RESET_ALL
                if cell == "R":
                    color = Fore.BLUE
                elif cell == "I":
                    color = Fore.GREEN
                elif cell == "C":
                    color = Fore.CYAN
                elif cell == "O":
                    color = Fore.LIGHTMAGENTA_EX
                elif cell == "*":
                    color = Fore.RED
                row.append(f"| {color}{cell}{Style.RESET_ALL} ")
            row.append("|")
            print("".join(row))
        print(separator)

    def check_arrow(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

    def on_press(self, key):
        if key == keyboard.Key.left:
            self.display(-1)
        elif key == keyboard.Key.right:
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

    def place_building(self, row, col, building_type):
        if 0 <= row < len(self.cells) and 0 <= col < len(self.cells[0]) and self.cells[row][col] == " ":
            self.cells[row][col] = building_type
            return True
        return False

    def find_connected_buildings(self, start_row, start_col):
        connected = set()
        to_check = [(start_row, start_col)]
        while to_check:
            r, c = to_check.pop(0)
            if (r, c) not in connected:
                connected.add((r, c))
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    new_r, new_c = r + dr, c + dc
                    if 0 <= new_r < len(self.cells) and 0 <= new_c < len(self.cells[0]):
                        if self.cells[new_r][new_c] == '*' or (new_r, new_c) == (start_row, start_col):
                            to_check.append((new_r, new_c))
                        elif self.cells[new_r][new_c] != ' ':
                            connected.add((new_r, new_c))
        return connected

def are_buildings_connected(board, pos1, pos2):
    visited = set()
    to_visit = [pos1]
    while to_visit:
        current = to_visit.pop(0)
        if current == pos2:
            return True
        if current in visited:
            continue
        visited.add(current)
        r, c = current
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(board.cells) and 0 <= nc < len(board.cells[0]):
                if board.cells[nr][nc] == '*' or (nr, nc) == pos2:
                    to_visit.append((nr, nc))
    return False

# Example usage:
# board = Board.create_board(20)
# board.display()
