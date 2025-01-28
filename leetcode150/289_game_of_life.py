# https://leetcode.com/problems/game-of-life/submissions/1523398840/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def gameOfLife(board: List[List[int]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    directions = [
        (-1, -1), (-1, 0), (-1, 1),  # Top-left, Top, Top-right
        (0, -1), (0, 1),  # Left, Right
        (1, -1), (1, 0), (1, 1)  # Bottom-left, Bottom, Bottom-right
    ]

    rows, cols = len(board), len(board[0])

    # Helper function to count live neighbors
    def count_live_neighbors(r, c):
        count = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and abs(board[nr][nc]) == 1:
                count += 1
        return count

    # Step 1: Apply rules and encode changes
    for r in range(rows):
        for c in range(cols):
            live_neighbors = count_live_neighbors(r, c)

            # Rule 1 and Rule 3: Live cell dies
            if board[r][c] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                board[r][c] = -1

            # Rule 4: Dead cell becomes live
            if board[r][c] == 0 and live_neighbors == 3:
                board[r][c] = 2

    # Step 2: Finalize the board
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 2:
                board[r][c] = 1
            elif board[r][c] == -1:
                board[r][c] = 0
