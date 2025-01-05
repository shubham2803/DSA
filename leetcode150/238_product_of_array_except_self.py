# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


def productExceptSelf(nums: List[int]) -> List[int]:
        left = 1
        out = [1] * len(nums)

        for i in range(len(nums)):
            out[i] *= left
            left *= nums[i]

        right = 1
        for i in range(len(nums) - 1, -1, -1):
            out[i] *= right
            right *= nums[i]

        return out

print(productExceptSelf([1,2,3,4]))
