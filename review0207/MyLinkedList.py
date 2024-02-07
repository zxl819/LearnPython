class ListNode:
    def __init__(self, next=None, val=0):
        self.next = next
        self.val = val

class MyLinkedList:
    def __init__(self):
        self.dummy = ListNode()
        self.size = 0
    
    def get(self, index: int):
        if index < 0 or index >= self.size:
            return -1
        
        current = self.dummy.next
        
        for i in range(index):
            current = current.next

        return current.val
    
    def addAtHead(self, val: int):
        self.dummy.next = ListNode(self.dummy.next, val)
        self.size += 1

    def addAtTail(self, val: int):
        current = self.dummy
        while current.next:
            current = current.next
        
        current.next = ListNode(val = val)
        self.size += 1

    
    def addAtIndex(self, index: int, val: int):
        if index < 0 or index > self.size:
            return -1
        current = self.dummy

        for i in range(index):
            current = current.next
        
        current.next = ListNode(current.next, val)
        self.size += 1
        return self.dummy.next
    
    def deleteAtIndex(self, index: int):
        if index < 0 or index >= self.size:
            return -1
        current = self.dummy # 应该为dummy

        for i in range(index):
            current = current.next
        
        current.next = current.next.next
        self.size -= 1



        


    
        
