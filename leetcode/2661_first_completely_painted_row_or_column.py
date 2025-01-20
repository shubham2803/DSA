# https://leetcode.com/problems/first-completely-painted-row-or-column/?envType=daily-question&envId=2025-01-20
from typing import List


def firstCompleteIndex(arr: List[int], mat: List[List[int]]) -> int:
    mat_map = {}

    m = len(mat)
    n = len(mat[0])

    for i in range(m):
        for j in range(n):
            mat_map[mat[i][j]] = (i, j)

    rows = [n] * m
    columns = [m] * n

    print(rows, columns)

    for i in range(0, len(arr)):
        r, c = mat_map[arr[i]]

        rows[r] -= 1
        columns[c] -= 1

        if rows[r] == 0 or columns[c] == 0:
            return i


arr = [6, 2, 3, 1, 4, 5]
mat = [[5, 1],
       [2, 4],
       [6, 3]]
print(firstCompleteIndex(arr, mat))
