#
# @lc app=leetcode.cn id=622 lang=python3
#
# [622] 设计循环队列
#
from collections import deque
# @lc code=start
class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear = 0
        self.data = [-1] * (k + 1)


    def enQueue(self, value: int) -> bool:
        if not self.isFull():
            self.data[self.rear] = value
        self.rear = (self.rear + 1) % len(self.data)
        return True


    def deQueue(self) -> bool:
        if self.isEmpty():
            return False

        val = self.data[self.front]
        self.front = (self.front + 1) % len(self.data)
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.data[self.front] 


    def Rear(self) -> int:
        return self.data[(self.rear - 1) % len(self.data)]


    def isEmpty(self) -> bool:
        return self.front == self.rear


    def isFull(self) -> bool:
        return (self.rear + 1) % len(self.data) == self.front
            



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
# @lc code=end

