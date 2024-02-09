class ListNode:
    def __init__ (self, next=None, val=0):
        self.next = next
        self.val = val
    
class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.size = 0

    def addAtHead(self, val):
        self.dummy.next = ListNode(self.dummy.next,val)
        self.size += 1
    def addAtTail(self, val):
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val = val)
        self.size += 1
    
    def get(self, index: int):
        if index < -1 or index >= self.size:
            return -1
        cur = self.dummy.next
        for i in range(index):
            cur = cur.next
        return cur.val
    
    def addAtIndex(self, index: int, val: int):
        if index < -1 or index > self.size:
            return -1
        cur = self.dummy
        for i in range(index):
            cur = cur.next
        cur.next = ListNode(cur.next, val)
        self.size += 1

    def deleteAtIndex(self, index: int):
        if index < -1 or index >= self.size:
            return -1
        cur = self.dummy
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1

    def create_list(self, elements: list[int]):
        self.dummy.next = ListNode(elements[0])
        cur =  self.dummy.next
        for element in elements:
            cur = ListNode(element)
            cur = cur.next
        return self.dummy.next
    
    def print_list(self):
        head = self.dummy.next
        elements = []
        while head:
            elements.append(head.val)
            head = head.next
        print(elements)

mylinkedlist = MyLinkedList()
mylinkedlist.addAtHead(1)
mylinkedlist.addAtTail(2)
mylinkedlist.addAtIndex(2, 3)
print(mylinkedlist.get(1))
mylinkedlist.print_list()
mylinkedlist.deleteAtIndex(2)
mylinkedlist.print_list()