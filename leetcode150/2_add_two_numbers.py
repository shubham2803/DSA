# https://leetcode.com/problems/add-two-numbers/description/?envType=study-plan-v2&envId=top-interview-150
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    new_node = ListNode(0, None)
    head = new_node
    carry = 0
    while l2 or l1:
        val_2 = val_1 = 0
        if l2:
            val_2 = l2.val
        if l1:
            val_1 = l1.val

        sum = val_1 + val_2 + carry
        if sum > 9:
            carry = 1
            current_node_val = sum % 10
        else:
            carry = 0
            current_node_val = sum

        next_node = ListNode(current_node_val, None)
        head.next = next_node
        head = head.next

        l2 = l2.next if l2 and l2.next else None
        l1 = l1.next if l1 and l1.next else None
    if carry:
        head.next = ListNode(1, None)
    return new_node.next