class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def swapPairs(self, head: ListNode):
        node0 = dummpy = ListNode(next=head)
        node1 = node0.next
        while node1 and node1.next:
            node2 = node1.next
            node3 = node2.next

            node0.next = node2
            node1.next = node3
            node2.next = node1
             
            node0 = node1
            node1 = node3
        return dummpy.next



            

        
