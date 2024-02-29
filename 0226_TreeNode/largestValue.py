class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: TreeNode):
        from collections import deque
        res = []
        queue = deque()
        queue.append(root)
       
        while queue:
            LevelMax = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if node.val > LevelMax:
                    LevelMax = node.val
            res.append(LevelMax)
        return res

                
        