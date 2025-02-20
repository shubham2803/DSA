# https://leetcode.com/problems/letter-tile-possibilities/description/?envType=daily-question&envId=2025-02-17
from collections import Counter


def numTilePossibilities(self, tiles: str) -> int:
    def backtrack(counter):
        total = 0
        for char in counter:
            if counter[char] > 0:
                counter[char] -= 1
                total += 1 + backtrack(counter)
                counter[char] += 1
        return total

    counter = Counter(tiles)
    return backtrack(counter)
