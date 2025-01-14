# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/description/?envType=daily-question&envId=2025-01-14

def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    c_map = {}
    count = 0
    out = []

    for i in range(len(A)):
        a_item = A[i]
        b_item = B[i]

        c_map[a_item] = c_map.get(a_item, 0) + 1
        c_map[b_item] = c_map.get(b_item, 0) + 1

        if a_item == b_item:
            count += 1
        else:
            if c_map[a_item] > 1:
                count += 1
            if c_map[b_item] > 1:
                count += 1
        out.append(count)

    return out
