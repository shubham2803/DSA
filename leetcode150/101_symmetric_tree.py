# https://leetcode.com/problems/symmetric-tree/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(self, root: Optional[TreeNode]) -> bool:
    def is_mirror(n1, n2):  # n1:left, n2:right
        if not n1 and not n2:
            return True

        if not n1 or not n2:
            return False

        return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

    return is_mirror(root.left, root.right)
