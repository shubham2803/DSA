# https://leetcode.com/problems/search-a-2d-matrix/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    start = 0
    end = len(matrix) * len(matrix[0]) - 1

    while start <= end:
        mid = (start + end) // 2
        row = mid // len(matrix[0])
        column = mid % len(matrix[0])
        if target == matrix[row][column]:
            return True
        if target > matrix[row][column]:
            start = mid + 1
        else:
            end = mid - 1
    return False
