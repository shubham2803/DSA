# https://leetcode.com/problems/reverse-nodes-in-k-group/?envType=study-plan-v2&envId=top-interview-150

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    def reverse(start: ListNode, end: ListNode) -> ListNode:
        prev, curr = None, start
        while curr != end:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev

    dummy = ListNode(0)
    dummy.next = head
    prev_group = dummy

    while True:
        kth = prev_group
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        next_group = kth.next
        start = prev_group.next
        kth.next = None
        reversed_group = reverse(start, None)

        prev_group.next = reversed_group
        start.next = next_group

        prev_group = start
