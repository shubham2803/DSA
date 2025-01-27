# https://leetcode.com/problems/valid-sudoku/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = [set() for _ in range(9)]
    columns = [set() for _ in range(9)]
    sub_boxes = [set() for _ in range(9)]

    for r in range(9):
        for c in range(9):
            num = board[r][c]
            if num == '.':
                continue

            sub_box_index = (r // 3) * 3 + (c // 3)

            if num in rows[r] or num in columns[c] or num in sub_boxes[sub_box_index]:
                return False

            rows[r].add(num)
            columns[c].add(num)
            sub_boxes[sub_box_index].add(num)

    return True
