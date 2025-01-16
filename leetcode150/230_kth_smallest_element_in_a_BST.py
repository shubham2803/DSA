# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/?envType=study-plan-v2&envId=top-interview-150
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    out = []

    def inorder(curr):
        if not curr:
            return None

        inorder(curr.left)
        out.append(curr.val)
        inorder(curr.right)

    inorder(root)
    return out[k - 1]
