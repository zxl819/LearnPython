class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

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


    
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        lenA, lenB = 0, 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
        curA, curB = headA, headB
        if lenA > lenB:
            curA, curB = curB, curA
            lenA, lenB = lenB, lenA
        
        for _ in range(lenB - lenA):
            curB =  curB.next
        
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
        