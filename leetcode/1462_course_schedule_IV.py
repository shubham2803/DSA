# https://leetcode.com/problems/course-schedule-iv/submissions/1522281658/?envType=daily-question&envId=2025-01-27
from typing import List


def checkIfPrerequisite(numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    graph = [[False] * numCourses for _ in range(numCourses)]
    for u, v in prerequisites:
        graph[u][v] = True

    for k in range(numCourses):
        for i in range(numCourses):
            for j in range(numCourses):
                graph[i][j] = graph[i][j] or graph[i][k] and graph[k][j]
    return [graph[i][j] for i, j in queries]
