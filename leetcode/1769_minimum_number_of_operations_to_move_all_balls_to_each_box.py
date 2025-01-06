# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/?envType=daily-question&envId=2025-01-06
from typing import List


def minOperations(self, boxes: str) -> List[int]:
    move = 0

    fw_movement = [0] * len(boxes)
    number_of_balls = 0

    for i in range(len(boxes)):
        fw_movement[i] = move + number_of_balls
        move += number_of_balls
        number_of_balls += int(boxes[i])

    move = 0
    number_of_balls = 0

    for j in reversed(range(len(boxes))):
        fw_movement[j] += move + number_of_balls
        move += number_of_balls
        number_of_balls += int(boxes[j])

    return fw_movement
