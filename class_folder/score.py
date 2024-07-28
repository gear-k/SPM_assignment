class Score:
    @staticmethod
    def calculate_score(board, mode):
        score = 0
        score += Score.calculate_industry_score(board)
        for r in range(len(board.cells)):
            for c in range(len(board.cells[0])):
                try:
                    if board.cells[r][c] == 'R':
                        score += Score.calculate_residential_score(board, r, c, mode)
                    elif board.cells[r][c] == 'C':
                        score += Score.calculate_commercial_score(board, r, c, mode)
                    elif board.cells[r][c] == 'O':
                        score += Score.calculate_park_score(board, r, c, mode)
                    elif board.cells[r][c] == '*':
                        score += Score.calculate_road_score(board, r, c, mode)
                except Exception as e:
                    print(f"Error calculating score for cell ({r}, {c}): {e}")
        return score

    @staticmethod
    def calculate_residential_score(board, row, col, mode):
        # Calculate the score for a residential building
        score = 0
        connected_buildings = [(row, col)]
        if mode == "Freeplay":
            connected_buildings = board.find_connected_buildings(row, col)
        
        adjacent_industry = any(board.cells[r][c] == 'I' for r, c in connected_buildings)

        if adjacent_industry:
            score = 1
        else:
            for r, c in connected_buildings:
                adjacent_positions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                for rr, cc in adjacent_positions:
                    if 0 <= rr < len(board.cells) and 0 <= cc < len(board.cells[0]):
                        if board.cells[rr][cc] == 'R' or board.cells[rr][cc] == 'C':
                            score += 1
                        elif board.cells[rr][cc] == 'O':
                            score += 2
        
        return score

    @staticmethod
    def calculate_industry_score(board):
        # Calculate the score for all industry buildings
        try:
            return sum(1 for r in range(len(board.cells)) for c in range(len(board.cells[0])) if board.cells[r][c] == 'I')
        except Exception as e:
            print(f"Error calculating industry score: {e}")
            return 0

    @staticmethod
    def calculate_commercial_score(board, row, col, mode):
        # Calculate the score for a commercial building
        score = 0
        connected_buildings = [(row, col)]
        if mode == "Freeplay":
            connected_buildings = board.find_connected_buildings(row, col)

        for r, c in connected_buildings:
            adjacent_positions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for rr, cc in adjacent_positions:
                if 0 <= rr < len(board.cells) and 0 <= cc < len(board.cells[0]) and board.cells[rr][cc] == 'C':
                    score += 1
        
        return score

    @staticmethod
    def calculate_park_score(board, row, col, mode):
        # Calculate the score for a park
        score = 0
        connected_buildings = [(row, col)]
        if mode == "Freeplay":
            connected_buildings = board.find_connected_buildings(row, col)

        for r, c in connected_buildings:
            adjacent_positions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
            for rr, cc in adjacent_positions:
                if 0 <= rr < len(board.cells) and 0 <= cc < len(board.cells[0]) and board.cells[rr][cc] == 'O':
                    score += 1
        
        return score

    @staticmethod
    def calculate_road_score(board, row, col, mode):
        # Calculate the score for a road
        score = 0
        if mode == "Freeplay":
            connected_roads = set()
            to_check = [(row, col)]
            while to_check:
                r, c = to_check.pop(0)
                if (r, c) not in connected_roads:
                    connected_roads.add((r, c))
                    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_r, new_c = r + dr, c + dc
                        if 0 <= new_r < len(board.cells) and 0 <= new_c < len(board.cells[0]) and board.cells[new_r][new_c] == '*':
                            to_check.append((new_r, new_c))
            score = len([r for r, c in connected_roads if r == row])
        else:
            for c in range(len(board.cells[0])):
                if board.cells[row][c] == '*':
                    score += 1

        return score

    @staticmethod
    def update_score_for_turn(board, mode):
        return Score.calculate_score(board, mode)
