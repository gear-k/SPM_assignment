import string
LETTERS = string.ascii_lowercase

class Board:
    def __init__(self, cells):
        self.cells = cells

    def create_board(cells):
        # Create the header row with letters
        header = ["   "] + [f" {LETTERS[i]} " for i in range(cells)] + ["\n"]
        seperator = "\n    " + "---+" * (cells -1) + "---"

        # Create the board with underscores and spaces
        board = [header]
        for i in range(cells):
            temp = [f"{i+1:2}  "]
            for j in range(cells):
                temp.append("  |")
            temp[-1] = "  "
            if i < cells - 1:
                temp[-1] += seperator
            board.append(temp)
        
        return board
