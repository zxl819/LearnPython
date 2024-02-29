class TreeNode:
    def __init__ (self, children=None, val=None):
        self.val = val
        self.children = children
    
class Solution:
    def NlevelTree(self, root: TreeNode):
        from collections import deque
        if not root:
            return []
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            level = []
            for i in range(len(queue)):
                node  = queue.popleft()
                for child in node.children:
                    queue.append(child)
                level.append(node.val)
            res.append(level)
        return res

