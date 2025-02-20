# https://leetcode.com/problems/find-unique-binary-string/description/?envType=daily-question&envId=2025-02-20

def findDifferentBinaryString(nums):
    return "".join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))
