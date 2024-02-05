class ListNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val =val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int):
        dummy_head = ListNode(next=head)
        current = dummy_head

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        
        return dummy_head.next

# 辅助函数：将列表转换为链表
def createLinkedList(elements):
    dummy_root = ListNode(0)
    ptr = dummy_root
    for element in elements:
        ptr.next = ListNode(element)
        ptr = ptr.next

    return dummy_root.next

# 辅助函数：打印链表
def printLinkedList(head):
    elements = []
    while head:
        elements.append(head.val)
        head = head.next
    print(elements)
head = [1,2,6,3,4,5,6]
val = 6
head = createLinkedList(head)
res = Solution().removeElements(head, val)
printLinkedList(res)