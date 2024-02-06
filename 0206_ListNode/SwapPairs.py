class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
<<<<<<< Updated upstream
    def swapPairs(self, head: ListNode):
=======
    def swapPairs(self, head: ListNode):
        dummpy_head = ListNode(next=head)
        current = dummpy_head
        while current.next and current.next.next:
            
            tmp1 = current.next.next
            tmp = current.next

            current.next = current.next.next
            current.next.next = 
    
            tmp.next = tmp1
            current.next = current.next.next

        return dummy_head.next
    
>>>>>>> Stashed changes
