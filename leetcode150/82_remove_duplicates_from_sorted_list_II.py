# https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    curr = head
    temp = ListNode(0)
    out = temp
    h_map = {}

    while head:
        h_map[head.val] = h_map.get(head.val, 0) + 1
        head = head.next

    while curr:
        if h_map[curr.val] == 1:
            temp.next = curr
            temp = temp.next
        curr = curr.next
    temp.next = None
    return out.next
