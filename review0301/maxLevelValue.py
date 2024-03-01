class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode):
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            value = - float("inf")
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.val > value:
                    value = node.val
            res.append(value)
        return res
        

            