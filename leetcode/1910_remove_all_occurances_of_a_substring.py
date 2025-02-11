# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/?envType=daily-question&envId=2025-02-11

def removeOccurrences(s: str, part: str) -> str:
    result_stack = []
    target_length = len(part)
    target_end_char = part[-1]

    for current_char in s:
        result_stack.append(current_char)

        if current_char == target_end_char and len(result_stack) >= target_length:
            if "".join(result_stack[-target_length:]) == part:
                del result_stack[-target_length:]

    return "".join(result_stack)