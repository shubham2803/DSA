# https://leetcode.com/problems/valid-parentheses/submissions/1510654382/?envType=study-plan-v2&envId=top-interview-150
def isValid(s: str) -> bool:
    b_map = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    stack = []

    for char in s:
        if char in b_map:
            stack.append(char)
        else:
            if not stack or b_map[stack.pop()] != char:
                return False

    return not stack
