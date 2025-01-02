# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150

def removeDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    for i in range(len(nums) - 1, 0, -1):
        if nums[i] == nums[i - 1]:
            nums.pop(i)
    return len(nums)
