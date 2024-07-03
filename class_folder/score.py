class Score:
    @staticmethod
    def calculate_score(board):
        # Calculate the total score for the board
        score = 0
        score += Score.calculate_industry_score(board, r, c)
        for r in range(len(board.cells)):
            for c in range(len(board.cells[0])):
                try:
                    if board.cells[r][c] == 'R':
                        score += Score.calculate_residential_score(board, r, c)
                    elif board.cells[r][c] == 'C':
                        score += Score.calculate_commercial_score(board, r, c)
                    elif board.cells[r][c] == 'O':
                        score += Score.calculate_park_score(board, r, c)
                    elif board.cells[r][c] == '*':
                        score += Score.calculate_road_score(board, r, c)
                except Exception as e:
                    print(f"Error calculating score for cell ({r}, {c}): {e}")
        return score

    @staticmethod
    def calculate_residential_score(board, row, col):
        # Calculate the score for a residential building
        score = 0
        adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        try:
            for r, c in adjacent_positions:
                if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]):
                    if board.cells[r][c] == 'R' or board.cells[r][c] == 'C':
                        score += 1
                    elif board.cells[r][c] == 'O':
                        score += 2
                    elif board.cells[r][c] == 'I':
                        score = 1
        except Exception as e:
            print(f"Error calculating residential score for cell ({row}, {col}): {e}")
        return score

    @staticmethod
    def calculate_industry_score(board, row, col):
        # Calculate the score for an industry building
        try:
            return sum(1 for r in range(len(board.cells)) for c in range(len(board.cells[0])) if board.cells[r][c] == 'I')
        except Exception as e:
            print(f"Error calculating industry score for cell ({row}, {col}): {e}")
            return 0

    @staticmethod
    def calculate_commercial_score(board, row, col):
        # Calculate the score for a commercial building
        score = 0
        adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        try:
            for r, c in adjacent_positions:
                if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]) and board.cells[r][c] == 'C':
                    score += 1
        except Exception as e:
            print(f"Error calculating commercial score for cell ({row}, {col}): {e}")
        return score

    @staticmethod
    def calculate_park_score(board, row, col):
        # Calculate the score for a park
        score = 0
        adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        try:
            for r, c in adjacent_positions:
                if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]) and board.cells[r][c] == 'O':
                    score += 1
        except Exception as e:
            print(f"Error calculating park score for cell ({row}, {col}): {e}")
        return score

    @staticmethod
    def calculate_road_score(board, row, col):
        # Calculate the score for a road
        score = 0
        try:
            for c in range(len(board.cells[0])):
                if board.cells[row][c] == '*':
                    score += 1
        except Exception as e:
            print(f"Error calculating road score for cell ({row}, {col}): {e}")
        return score
