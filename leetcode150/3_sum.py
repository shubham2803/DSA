from typing import List


def threeSum(nums):
    nums.sort()  # Sort the array
    result = []  # To store the final triplets

    for i in range(len(nums) - 2):  # Loop over each number, leaving space for two more numbers
        # Skip duplicate elements to avoid repeating triplets
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Use two pointers to find pairs that sum to -nums[i]
        left, right = i + 1, len(nums) - 1

        while left < right:
            total = nums[i] + nums[left] + nums[right]

            if total == 0:  # Found a valid triplet
                result.append([nums[i], nums[left], nums[right]])
                # Move both pointers to the next unique values
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
            elif total < 0:  # Need a larger sum, move left pointer
                left += 1
            else:  # Need a smaller sum, move right pointer
                right -= 1

    return result


print(threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))