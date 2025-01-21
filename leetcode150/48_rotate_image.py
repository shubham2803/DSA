# https://leetcode.com/problems/rotate-image/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)

    for i in range(rows):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    matrix[:] = [x[::-1] for x in matrix]
