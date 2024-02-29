class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node):
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            N = len(queue)
            pre = None
            for i in range(N):
                node = queue.popleft()
                if pre:
                    pre.next = node
                pre = node

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root

                

