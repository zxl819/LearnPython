#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)


    def get(self, index: int) -> int:
        cur = self.head
        if index < 0 or index >= self.size:
            return -1
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

        


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)



    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        
        elif index < 0:
            index = 0
        cur = self.head
        for _ in range(index):
            cur = cur.next

        addNode = ListNode(val)
        addNode.next = cur.next
        cur.next = addNode
        self.size += 1



    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        if index < 0 or index >= self.size:
            return
        
        self.size -= 1
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

