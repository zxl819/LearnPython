class ListNode:
    def __init__(self, next=None, val = 0):
        self.next = None
        self.val = val

class Solution:
    def removeElement(self , head: ListNode, val: int):
        dummpy_head = ListNode(next = head)
        current = dummpy_head

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummpy_head.next

head = [1,2,6,3,4,5,6]
val = 6

print(Solution().removeElement(head, val))