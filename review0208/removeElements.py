class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def removeElements(self, head: ListNode, val: int):
        dummy = ListNode(next=head)
        cur  = dummy
        while (cur.next != None):
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        
        return dummy.next
    
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
    

head = creat_list([1,2,6,3,4,5,6])
val = 0
new = Solution().removeElements(head, val)
print_list(new)