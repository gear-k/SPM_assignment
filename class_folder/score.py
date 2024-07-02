class Score:
    @staticmethod
    def calculate_score(board):
        score = 0
        for r in range(len(board.cells)):
            for c in range(len(board.cells[0])):
                if board.cells[r][c] == 'R':
                    score += Score.calculate_residential_score(board, r, c)
                elif board.cells[r][c] == 'I':
                    score += Score.calculate_industry_score(board, r, c)
                elif board.cells[r][c] == 'C':
                    score += Score.calculate_commercial_score(board, r, c)
                elif board.cells[r][c] == 'O':
                    score += Score.calculate_park_score(board, r, c)
                elif board.cells[r][c] == '*':
                    score += Score.calculate_road_score(board, r, c)
        return score

    def calculate_residential_score(board, row, col):
        score = 0
        adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for r, c in adjacent_positions:
            if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]):
                if board.cells[r][c] == 'R' or board.cells[r][c] == 'C':
                    score += 1
                elif board.cells[r][c] == 'O':
                    score += 2
                elif board.cells[r][c] == 'I':
                    score += 1
        return score

    def calculate_industry_score(board, row, col):
        return sum(1 for r in range(len(board.cells)) for c in range(len(board.cells[0])) if board.cells[r][c] == 'I')

    def calculate_commercial_score(board, row, col):
        score = 0
        adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for r, c in adjacent_positions:
            if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]) and board.cells[r][c] == 'C':
                score += 1
        return score

    def calculate_park_score(board, row, col):
        score = 0
        adjacent_positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        for r, c in adjacent_positions:
            if 0 <= r < len(board.cells) and 0 <= c < len(board.cells[0]) and board.cells[r][c] == 'O':
                score += 1
        return score

    def calculate_road_score(board, row, col):
        score = 0
        for c in range(len(board.cells[0])):
            if board.cells[row][c] == '*':
                score += 1
        return score