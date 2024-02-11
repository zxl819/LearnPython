class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        left = right = dummy = ListNode(next=head)
        for i in range(n):
            right = right.next
        
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next

        return dummy.next