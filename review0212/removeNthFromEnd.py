class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        left = right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next
