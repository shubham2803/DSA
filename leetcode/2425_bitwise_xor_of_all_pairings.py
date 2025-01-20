# https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=daily-question&envId=2025-01-16
def xorAllNums(nums1: List[int], nums2: List[int]) -> int:
    nums1_xor = 0
    if len(nums2) % 2 == 1:
        for num in nums1:
            nums1_xor ^= num

    nums2_xor = 0
    if len(nums1) % 2 == 1:
        for num in nums2:
            nums2_xor ^= num

    return nums1_xor ^ nums2_xor
