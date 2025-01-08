# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150/
from typing import List


def twoSum(self, numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while i < j:
        curr = numbers[i] + numbers[j]

        if curr == target:
            return [i + 1, j + 1]
        if curr > target:
            j -= 1
        else:
            i += 1
    return []


numbers = [5, 25, 75]
target = 100

print(twoSum(numbers, target))
