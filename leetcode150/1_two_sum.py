# https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150

def twoSum(nums: List[int], target: int) -> List[int]:
    n_map = {}

    for i in range(len(nums)):
        remain = target - nums[i]

        if remain in n_map:
            return [n_map[remain], i]
        n_map[nums[i]] = i
    return []
