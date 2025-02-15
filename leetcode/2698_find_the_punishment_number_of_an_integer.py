# https://leetcode.com/problems/find-the-punishment-number-of-an-integer/?envType=daily-question&envId=2025-02-15
class Solution:
    def punishmentNumber(self, n: int) -> int:
        def partition(x, target):
            if x == target: return True
            if x == 0: return target == 0
            for m in (10, 100, 1000):
                if partition(x // m, target - x % m):
                    return True
            return False

        return sum(x for i in range(1, n + 1) if partition(x := i * i, i))
