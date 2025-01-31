# https://leetcode.com/problems/making-a-large-island/description/?envType=daily-question&envId=2025-01-31
from collections import defaultdict, deque
from typing import List


def largestIsland(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    islands = defaultdict(int)

    def bfs(i, j, idx):
        queue = deque([(i, j)])
        grid[i][j] = idx
        while queue:
            r, c = queue.popleft()
            islands[idx] += 1
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    queue.append((nr, nc))
                    grid[nr][nc] = idx

    def connectedIslands(i, j):
        curArea = 1
        visited = set()
        for r, c in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            if 0 <= r < m and 0 <= c < n and grid[r][c] != 0 and grid[r][c] not in visited:
                curArea += islands[grid[r][c]]
                visited.add(grid[r][c])
        return curArea

    # Step 1: Label islands
    idx = 2
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                bfs(i, j, idx)
                idx += 1

    maxArea = max(islands.values()) if islands else 0

    # Step 2: Check water cells for potential island merging
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 0:
                maxArea = max(maxArea, connectedIslands(i, j))

    return maxArea
