# https://leetcode.com/problems/product-of-the-last-k-numbers/?envType=daily-question&envId=2025-02-14

class ProductOfNumbers:

    def __init__(self):
        self.stream = [1]
        self.l = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.stream = [1]
            self.l = 1
        else:
            self.stream.append(self.stream[-1] * num)
            self.l += 1

    def getProduct(self, k: int) -> int:
        if self.l <= k:
            return 0
        else:
            return self.stream[-1] // self.stream[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
