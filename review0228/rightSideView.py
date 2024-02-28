# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: TreeNode):
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            N = len(queue)
            for i in range(N):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == N - 1:
                    res.append(node.val)
        return res
                    
        