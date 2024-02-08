class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val
class Solution:
    def reverseList(self, head: ListNode):
        pre = None
        cur = head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

def creat_list(elements: list[int]):
        head = ListNode(elements[0])
        cur = head
        for element in elements:
            cur.next = ListNode(val = element)
            cur = cur.next
        return head

def print_list(head):
        elements =[]
        while head:
            elements.append(head.val)
            head = head.next
        print(elements)  
    
head = [1,2,3,4,5]
new = creat_list(head)
a = Solution().reverseList(new)
print_list(a)


    