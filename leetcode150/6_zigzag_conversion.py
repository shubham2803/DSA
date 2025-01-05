# https://leetcode.com/problems/zigzag-conversion/?envType=study-plan-v2&envId=top-interview-150
def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    idx = 0
    f = 1

    out = [[] for _ in range(numRows)]

    for ele in s:
        out[idx].append(ele)
        if idx == 0:
            f = 1
        elif idx == numRows - 1:
            f = -1
        idx += f

    for i in range(len(out)):
        out[i] = ''.join(out[i])

    return ''.join(out)


print(convert('PAYPALISHIRING', 3))
