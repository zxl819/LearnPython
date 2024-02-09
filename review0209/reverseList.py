class ListNode:
    def __init__ (self, next=None, val=0):
        self.next = next
        self.val = val

class Solution:
    def reverseList(self):
        self.pre = None
        cur = self.head
        while cur:
            tmp = cur.next
            cur.next = self.pre
            self.pre = cur
            cur = tmp
        return self.pre

    def create_list(self, elements: list[int]):
        self.head = ListNode(elements[0])
        cur =  self.head
        for element in elements:
            cur.next = ListNode(val = element)
            cur = cur.next
        return self.head
    
    def print_list(self):
        elements =[]
        cur = self.pre # 使用局部变量cur遍历链表，避免修改self.head
        while cur.next:
            elements.append(cur.val)
            cur = cur.next
        print(elements)

head = [1,2,3,4,5]
mylist = Solution()
mylist.create_list(head)
mylist.reverseList()
#mylist.create_list()
mylist.print_list()


        
    

    


    



