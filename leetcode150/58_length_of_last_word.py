# https://leetcode.com/problems/length-of-last-word/description/?envType=study-plan-v2&envId=top-interview-150

def lengthOfLastWord(s: str) -> int:
    last_count = 0
    char_on = False
    for i in s[::-1]:
        if i != ' ':
            last_count += 1
            char_on = True
        if i == ' ':
            if char_on:
                break
    return last_count
