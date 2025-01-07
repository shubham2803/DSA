# https://leetcode.com/problems/jump-game-ii/description/?envType=study-plan-v2&envId=top-interview-150
def jump(self, nums: List[int]) -> int:
    if len(nums) <= 1:
        return 0
    n = len(nums)
    jump_count = 0
    finish = 0
    farthest = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])

        if i == finish:
            jump_count += 1
            finish = farthest

            if finish >= (n - 1):
                break
    return jump_count