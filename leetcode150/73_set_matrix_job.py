# https://leetcode.com/problems/set-matrix-zeroes/description/?submissionId=1304893568
from typing import List


def setZeroes(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows_to_be_0 = {}
    columns_to_be_0 = {}

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == 0:
                rows_to_be_0[r] = True
                columns_to_be_0[c] = True

    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if r in rows_to_be_0:
                matrix[r][c] = 0
            if c in columns_to_be_0:
                matrix[r][c] = 0
