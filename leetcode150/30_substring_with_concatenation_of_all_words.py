# https://leetcode.com/problems/substring-with-concatenation-of-all-words/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter
from typing import List


def findSubstring(self, s: str, words: List[str]) -> List[int]:
    if not s or not words:
        return []

    word_length = len(words[0])
    word_count = len(words)
    word_map = Counter(words)
    result = []
    total_length = word_length * word_count

    for i in range(word_length):
        left = i
        right = i
        current_map = Counter()

        while right + word_length <= len(s):
            word = s[right:right + word_length]
            right += word_length

            if word in word_map:
                current_map[word] += 1
                while current_map[word] > word_map[word]:
                    current_map[s[left:left + word_length]] -= 1
                    left += word_length

                if right - left == total_length:
                    result.append(left)
            else:
                current_map.clear()
                left = right

    return result
