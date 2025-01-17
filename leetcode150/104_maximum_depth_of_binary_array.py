# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
        return 0

    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
