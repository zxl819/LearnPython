# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_r = self.reverse(l1)
        l2_r = self.reverse(l2)
        return self.reverse(self.addTwoNumbers2(l1_r, l2_r))

    def addTwoNumbers2(self, l1: ListNode, l2: ListNode, carry = 0):
        if l1 is None and l2 is None:
            return ListNode(carry) if carry else None
        if l1 is None:
            l1, l2 = l2, l1
        carry += l1.val + (l2.val if l2 else 0)
        l1.val = carry % 10
        l1.next = self.addTwoNumbers2(l1.next, (l2.next if l2 else None), carry // 10)
        return l1


    def reverse(self, head: ListNode):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
            

