class Score:
    @staticmethod
    def calculate_score(board):
        score = 0
        score += Score.calculate_industry_score(board)
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
        score = 0
        adjacent_industry = False
        connected_buildings = board.find_connected_buildings(row, col)

        for r, c in connected_buildings:
            if board.cells[r][c] == 'I':
                adjacent_industry = True
                break

        if adjacent_industry:
            score = 1
        else:
            for r, c in connected_buildings:
                if board.cells[r][c] == 'R' or board.cells[r][c] == 'C':
                    score += 1
                elif board.cells[r][c] == 'O':
                    score += 2

        return score

    @staticmethod
    def calculate_industry_score(board):
        try:
            return sum(1 for r in range(len(board.cells)) for c in range(len(board.cells[0])) if board.cells[r][c] == 'I')
        except Exception as e:
            print(f"Error calculating industry score: {e}")
            return 0

    @staticmethod
    def calculate_commercial_score(board, row, col):
        score = 0
        connected_buildings = board.find_connected_buildings(row, col)

        for r, c in connected_buildings:
            if board.cells[r][c] == 'C':
                score += 1
            elif board.cells[r][c] == 'R':
                score += 1

        return score

    @staticmethod
    def calculate_park_score(board, row, col):
        score = 0
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            new_r, new_c = row + dr, col + dc
            if 0 <= new_r < len(board.cells) and 0 <= new_c < len(board.cells[0]):
                if board.cells[new_r][new_c] == 'O':
                    score += 1
        return score

    @staticmethod
    def calculate_road_score(board, row, col):
        score = 0
        road_cluster = set()

        for c in range(len(board.cells[0])):
            if board.cells[row][c] == '*' and (row, c) not in road_cluster:
                connected_roads = board.find_connected_buildings(row, c)
                road_cluster.update(connected_roads)

        score += len(road_cluster)
        return score

    @staticmethod
    def update_score_for_turn(board):
        return Score.calculate_score(board)
