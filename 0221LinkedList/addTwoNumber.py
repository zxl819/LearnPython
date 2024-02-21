class ListNode:
    def __init__(self, next = None, val = 0):
        self.next = next
        self.val = val

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        dummy = ListNode(next = l2)
        len1 = 0
        len2 = 0
        cur = l1
        while cur:
            cur = cur.next
            len1 += 1
        cur = l2
        while cur:
            cur = cur.next
            len2 += 1
        cur1 = l1
        cur2 = l2
        if len1 > len2:
            cur1, cur2 = cur2, cur1
            len1, len2 = len2, len1

        while cur2:
            while cur1:
                newVal = cur1.val + cur2.val
                if newVal > 9:
                    newVal -= 10
                    cur2.next.val += 1
                cur1 = cur1.next
                cur2 = cur2.next
                dummy.next = ListNode(val = newVal)
            dummy.next = cur2.next
            cur2 = cur2.next
        return dummy.next
        