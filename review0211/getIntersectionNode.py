class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        lenA = lenB = 0
        cur = ListNode(next=headA)
        while cur:
            cur = cur.next
            lenA += 1
        cur = ListNode(next=headB)
        while cur:
            lenB += 1
            cur = cur.next
        if lenA > lenB:
            lenA, lenB = lenB, lenA
            curA, curB = headB, headA
        
        for _ in range(lenB - lenA):
            curB = curB.next
        
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        
        return None
            
