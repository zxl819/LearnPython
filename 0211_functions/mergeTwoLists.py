# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        head1 = list1
        head2 = list2
        dummy = ListNode()
        tail = dummy
        while head1 and head2:
            if head1.val < head2.val:
                tail.next = head1
                head1 = head1.next
            else:
                tail.next = head2
                head2 = head2.next
            tail = tail.next

        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2
        
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

def print_list(head: ListNode):
    elements = []
    cur = head  # 使用局部变量cur遍历链表，避免修改self.head
    while cur:
        elements.append(cur.val)
        cur = cur.next
    print(elements)

l1 = [1,2,4]
l2 = [1,3,4]
list1 = createList(l1)
list2 = createList(l2)
node0 = Solution().mergeTwoLists(list1, list2)
print_list(node0)
