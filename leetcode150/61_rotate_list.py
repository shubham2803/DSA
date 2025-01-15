# https://leetcode.com/problems/rotate-list/description/?envType=study-plan-v2&envId=top-interview-150
from typing import Optional


class ListNode:
    pass


def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0:
        return head

    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    k %= length
    if k == 0:
        return head

    new_tail_position = length - k - 1
    new_head_position = length - k

    current = head
    for _ in range(new_tail_position):
        current = current.next
    new_tail = current
    new_head = current.next

    new_tail.next = None
    current = new_head
    while current.next:
        current = current.next
    current.next = head

    return new_head
