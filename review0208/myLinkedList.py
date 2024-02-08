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
        cur = self.dummy.next
        for i in range(index):
            cur = cur.next
        return cur.val
    
    def addAtHead(self, val: int):
        cur = self.dummy
        cur.next = ListNode(cur.next,val)
        self.size += 1

    def addAtTail(self, val: int):
        cur = self.dummy
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val = val)
        self.size += 1
    
    def addAtIndex(self, index: int, val: int):
        if index < 0 or index > self.size:
            return -1
        
        cur = self.dummy
        for i in range(index):
            cur = cur.next
        cur.next = ListNode(cur.next, val)
        self.size += 1

    def deleteAtIndex(self, index: int):
        if index < 0 or index > self.size:
            return -1
        cur = self.dummy
        for i in range(index):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
    
    def print_list(self):  #在 MyLinkedList 类中，您定义的 print_list 方法应该是一个实例方法，而不是静态方法或类方法。实例方法需要通过 self 访问实例的属性和方法。但在您的 print_list 方法定义中，您尝试将它作为一个静态方法（没有使用 self），并且尝试直接传递 head 参数，这与您的类设计不兼容。
        elemnets = []
        head = self.dummy.next
        while head:
            elemnets.append(head.val)
            head = head.next
        return elemnets
        
    

myList = MyLinkedList()
myList.addAtHead(3)
myList.addAtHead(2)
myList.addAtTail(1)
myList.addAtTail(0)
myList.addAtIndex(1, 5)
myList.deleteAtIndex(4)

print(myList.print_list())


# def creat_list(elements: list[int]):
#         head = ListNode(elements[0])
#         cur = head
#         for element in elements:
#             cur.next = ListNode(val = element)
#             cur = cur.next
#         return head

# def print_list(head):
#         elements =[]
#         while head:
#             elements.append(head.val)
#             head = head.next
#         print(elements)    



