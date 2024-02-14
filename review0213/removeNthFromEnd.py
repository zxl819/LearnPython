class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        left = dummy = right = ListNode(next=head)
        