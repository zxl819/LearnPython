class ListNode:
    def __init__ (self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def swapPairs(self):
        node0 = self.dummy = ListNode(next=self.head.next)
        node1 = node0.next
        while node1 and node1.next:
            node2 = node1.next
            node3 = node2.next

            node2.next = node1
            node1.next = node3
            node0.next = node2

            node0 = node1
            node1 = node3 

        return self.dummy.next

    def create_list(self, elements: list[int]):
        self.head = ListNode(elements[0])
        cur =  self.head
        for element in elements:
            cur.next = ListNode(val = element)
            cur = cur.next
        return self.head.next
    
    def print_list(self):
        elements =[]
        cur = self.dummy.next # 使用局部变量cur遍历链表，避免修改self.head
        while cur:
            elements.append(cur.val)
            cur = cur.next
        print(elements)

head = [1,2,3,4]
mylist = Solution()
mylist.create_list(head)
mylist.swapPairs()
#mylist.create_list()
mylist.print_list()


        
    

    


    



