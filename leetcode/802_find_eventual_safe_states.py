# https://leetcode.com/problems/find-eventual-safe-states/description/?envType=daily-question&envId=2025-01-24
from typing import List


def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    safe = [0] * n

    def dfs(node):
        if safe[node] > 0:
            return safe[node]

        safe[node] = 2

        for neighbor in graph[node]:
            if safe[neighbor] == 2 or dfs(neighbor) == 2:
                return 2

        safe[node] = 1
        return 1

    for i in range(n):
        if safe[i] == 0:
            dfs(i)

    return [i for i in range(n) if safe[i] == 1]
