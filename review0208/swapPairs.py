class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def swapPairs(self, head: ListNode):
        node0 = dummy = ListNode(next=head)
        node1 = node0.next
         
        while node1 and node1.next:
             node2 = node1.next
             node3 = node2.next

             node2.next = node1
             node1.next = node3
             node0.next = node2

             node0 = node1
             node1 = node3 

        return dummy.next
        


def creat_list(elements: list[int]):
        head = ListNode(elements[0])
        cur = head
        for element in elements:
            cur.next = ListNode(val = element)
            cur = cur.next
        return head.next

def print_list(head):
        elements =[]
        while head:
            elements.append(head.val)
            head = head.next
        print(elements) 


head = [1,2,3,4]
new = creat_list(head)
a = Solution().swapPairs(new)
print_list(a)