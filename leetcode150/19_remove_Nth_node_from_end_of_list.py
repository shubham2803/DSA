# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    current_node = head
    prev_node = head
    for _ in range(n):
        current_node = current_node.next

    if not current_node:
        return head.next

    while current_node.next:
        current_node = current_node.next
        prev_node = prev_node.next

    prev_node.next = prev_node.next.next
    return head
