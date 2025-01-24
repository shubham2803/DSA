# https://leetcode.com/problems/reverse-linked-list-ii/?envType=study-plan-v2&envId=top-interview-150
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    temp = ListNode(0)
    temp_head = temp
    x = head

    left_nodes = ListNode(0)
    left_ = left_nodes
    for _ in range(left - 1):
        left_nodes.next = x
        left_nodes = left_nodes.next
        x = x.next
    left_nodes.next = None

    for _ in range(right - left + 1):
        temp.next = x
        x = x.next
        temp = temp.next
    temp.next = None

    curr = temp_head.next
    prev = None
    while curr is not None:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node

    right_nodes = ListNode(0)
    right_ = right_nodes
    while x:
        right_nodes.next = x
        x = x.next
        right_nodes = right_nodes.next
    right_nodes.next = None

    res = ListNode(0)
    res_head = res

    while left_:
        res.next = left_
        left_ = left_.next
        res = res.next

    prev = prev
    while prev:
        res.next = prev
        prev = prev.next
        res = res.next

    right_ = right_.next
    while right_:
        res.next = right_
        right_ = right_.next
        res = res.next
    res_head = res_head.next
    return res_head.next if res_head else None
