class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        left =  right = dummy = ListNode(next=head)
        for _ in range(n):
            right = right.next
        while right.next:
            left = left.next
            right = right.next
        left.next = left.next.next
        return dummy.next



def createList(elements: list):
    if not elements:
        return None
    dummy = ListNode()
    cur = dummy
    for element in elements:
        cur.next = ListNode(val=element)
        cur = cur.next
    return dummy.next

def printList(head: ListNode):
    elements = []
    while head:
        elements.append(head.val)
        head =head.next
    print(elements)

    
head = [1,2,3,4,5]
head2 = createList(head)
n = 2
Solution().removeNthFromEnd(head2, n)      
printList(head2)  
