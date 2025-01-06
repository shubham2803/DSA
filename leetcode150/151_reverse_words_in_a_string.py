# https://leetcode.com/problems/reverse-words-in-a-string/?envType=study-plan-v2&envId=top-interview-150
def reverseWords(s: str) -> str:
    out = [''] * len(s)

    b = 0
    e = len(s) - 1

    for i in range(len(s)):
        if s[i] != ' ':
            b = i
            break

    for j in range(len(s) - 1, -1, -1):
        if s[j] != ' ':
            e = j + 1
            break
    words = []
    word = ''
    for i in range(b, e):
        if s[i] != ' ':
            word += s[i]
        else:
            if word != '':
                words.append(word)
            word = ''

    words.append(word)
    return ' '.join(words[::-1])

print(reverseWords("a good   example"))
