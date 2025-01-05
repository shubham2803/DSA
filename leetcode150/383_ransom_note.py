# https://leetcode.com/problems/ransom-note/submissions/1498336013/?envType=study-plan-v2&envId=top-interview-150
def canConstruct(ransomNote: str, magazine: str) -> bool:
    ransom_map = {}
    magazine_map = {}
    for x in ransomNote:
        ransom_map[x] = ransom_map.get(x, 0) + 1

    for y in magazine:
        magazine_map[y] = magazine_map.get(y, 0) + 1

    for k, v in ransom_map.items():
        if magazine_map.get(k, 0) < v:
            return False

    return True


print(canConstruct("a", "b"))
