# https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/description/?envType=daily-question&envId=2025-01-28

def findMaxFish(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    m = len(grid)
    n = len(grid[0])
    maxFish = 0

    def dfs(i, j, m, n):
        fish = 0

        if grid[i][j] == 0:
            return fish

        fish += grid[i][j]
        grid[i][j] = -1

        for dir in directions:
            nr = i + dir[0]
            nc = j + dir[1]
            if 0 <= nr < m and 0 <= nc < n:
                if grid[nr][nc] > 0:
                    fish += dfs(nr, nc, m, n)

        return fish

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                continue
            maxFish = max(maxFish, dfs(i, j, m, n))

    return maxFish
