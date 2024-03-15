class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

head = [1,2,3,4,5]
headnew = createList(head)
node0 = Solution().reverseList(headnew)
print_list(node0)
