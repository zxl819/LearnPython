class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def reverseList(self, head: ListNode):
        # self.dummy_head = ListNode(next=head)
        # current = self.dummy_head
        # res =[]

        # while current.next:
        #     res.append(current.val)
        #     current = current.next
        #     i += 1
        # #return res
        # a = reversed(res)

        # for j in range(i):
        #     current.val = res[j]
        #     current = current.next
        
        # return self.dummy_head
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
            





    
