class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def reverseList(self, head: ListNode):
        pre = None
        cur = head
        while cur: #当cur = None结束
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre # 三个指针轮
            
            


