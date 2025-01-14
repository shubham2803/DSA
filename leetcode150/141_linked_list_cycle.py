# https://leetcode.com/problems/linked-list-cycle/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head: Optional[ListNode]) -> bool:
    n_map = {}

    while head is not None:
        if head not in n_map:
            n_map[head] = True
        else:
            return True
        head = head.next
    return False
