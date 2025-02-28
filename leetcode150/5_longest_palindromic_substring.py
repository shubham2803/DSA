# https://leetcode.com/problems/longest-palindromic-substring/description/?envType=study-plan-v2&envId=top-interview-150
def longestPalindrome(s):
    """
    :type s: str
    :rtype: str
    """
    longest = ""
    maxLength = 1
    start = 0
    low = 0
    high = 0
    string = s
    length = len(s)
    for i in range(1, length):
        low = i - 1
        high = i
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1

        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
            start = low
            maxLength = high - low + 1

        low = i - 1
        high = i + 1
        while low >= 0 and high < length and string[low] == string[high]:
            low -= 1
            high += 1
        low += 1
        high -= 1
        if string[low] == string[high] and high - low + 1 > maxLength:
            start = low
            maxLength = high - low + 1

    return string[start:start + maxLength]
