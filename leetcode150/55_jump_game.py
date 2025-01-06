# https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150
def canJump(nums: List[int]) -> bool:
    if len(nums) < 2:
        return True

    max_jump = nums[0]
    for i in range(1, len(nums)):
        if max_jump == 0:
            return False
        max_jump -= 1
        if max_jump < nums[i]:
            max_jump = nums[i]
        if (i + max_jump + 1) >= len(nums):
            return True
    return False
