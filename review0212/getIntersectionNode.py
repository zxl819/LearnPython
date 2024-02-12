class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        lenA, lenB = 0, 0
        cur = headA
        while cur:
            cur = cur.next
            lenA += 1
        cur = headB
        while cur:
            cur = cur.next
            lenB += 1
        if lenA > lenB:
            lenA, lenB = lenB, lenA
            headA, headB = headB, headA
        curA = headA
        curB = headB
        for _ in range(lenB - lenA):
            curB = curB.next
        while curA:
            if curA == curB:
                return curA
            else:
                curA = curA.next
                curB = curB.next
        return None
