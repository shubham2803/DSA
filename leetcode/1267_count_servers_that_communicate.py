# https://leetcode.com/problems/count-servers-that-communicate/description/?envType=daily-question&envId=2025-01-23
def countServers(grid):
    m = len(grid)
    n = len(grid[0])

    row_count = [0] * m
    col_count = [0] * n

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                row_count[i] += 1
                col_count[j] += 1

    result = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                if row_count[i] > 1 or col_count[j] > 1:
                    result += 1

    return result
