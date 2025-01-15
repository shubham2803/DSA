# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(head: Optional[ListNode], x: int) -> Optional[ListNode]:
    less = ListNode(0)
    more = ListNode(0)
    less_temp = less
    more_temp = more

    while head:
        if head.val < x:
            less.next = head
            less = less.next
        else:
            more.next = head
            more = more.next
        head = head.next
    less.next = more_temp.next
    more.next = None
    return less_temp.next
