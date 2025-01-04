from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    out = []
    curr_w = 0
    grp = []

    for word in words:
        if curr_w + len(word) + len(grp) > maxWidth:
            spaces_needed = maxWidth - curr_w
            if len(grp) == 1:
                out.append(grp[0] + ' ' * spaces_needed)
            else:
                even_space = spaces_needed // (len(grp) - 1)
                extra_space = spaces_needed % (len(grp) - 1)

                line = ""
                for i in range(len(grp) - 1):
                    line += grp[i] + ' ' * (even_space + (1 if i < extra_space else 0))
                line += grp[-1]
                out.append(line)

            grp = [word]
            curr_w = len(word)
        else:
            grp.append(word)
            curr_w += len(word)

    last_line = ' '.join(grp)
    last_line += ' ' * (maxWidth - len(last_line))
    out.append(last_line)
    print([len(i) for i in out])
    return out


# Test cases
print(fullJustify(["a", "b", "c", "d", "e"], 3))  # ["a  b  c", "d  e  "]
print(fullJustify(["Listen", "to", "many,", "speak", "to", "a", "few."], 6))
print(fullJustify(["What", "must", "be", "shall", "be."], 5))
print(fullJustify(
    ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
     "is", "everything", "else", "we", "do"], 20))
print(fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(fullJustify(["What", "must", "be", "acknowledgment", "shall", "be"], 16))
print(fullJustify(
    ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do", "for",
     "your", "country"], 16))
