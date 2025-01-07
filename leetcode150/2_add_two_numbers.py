# https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    out = ListNode(0, None)
    head = out
    carry = 0

    while l1 is not None and l2 is not None:
        curr_val = l1.val + l2.val + carry

        l1 = l1.next if l1 and l1.next else None
        l2 = l2.next if l2 and l2.next else None

        if curr_val > 9:
            carry = 1
            curr_val = curr_val % 10
        else:
            carry = 0

        head.next = ListNode(curr_val, None)
        head = head.next

    while l1 is not None:
        val = l1.val + carry

        if val > 9:
            val = val % 10
            carry = 1
        else:
            carry = 0
        if l1:
            head.next = ListNode(val, None)
            head = head.next

        l1 = l1.next if l1 and l1.next else None

    while l2 is not None:
        val = l2.val + carry
        carry = 0

        if val > 9:
            val = val % 10
            carry = 1
        else:
            carry = 0
        if l2:
            head.next = ListNode(val, None)
            head = head.next

        l2 = l2.next if l2 and l2.next else None

    if carry:
        head.next = ListNode(carry, None)

    return out.next

