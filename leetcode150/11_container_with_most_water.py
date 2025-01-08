# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=top-interview-150

def maxArea(self, height: List[int]) -> int:
    n = len(height)
    s = 0
    e = n - 1
    out = 0

    while s < e:
        w = e - s
        h = min(height[s], height[e])

        if height[s] < height[e]:
            s += 1
        else:
            e -= 1

        out = max(out, w * h)

    return out
