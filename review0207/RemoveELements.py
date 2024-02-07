class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def removeElemnets(self, head: ListNode, val: int):
        dummy = ListNode(next=head)
        cur =  dummy.next
        while cur:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return dummy.next
                