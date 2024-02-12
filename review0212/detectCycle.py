class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def detectCycle(self, head: ListNode):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None