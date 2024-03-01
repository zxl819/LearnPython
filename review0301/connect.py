
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Node) -> Node:
        if not root:
            return None
        from collections import deque
        queue = deque()
        queue.append(root)
        while queue:
            pre = None
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                if pre:
                    pre.next = node
                pre = node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                