class TreeNode:
    def __init__(self, children = None, val=0):
        self.children = children
        self.val = val

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
                level.append(node.val)
            res.append(level)
        return res
    
                
        