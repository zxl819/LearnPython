class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def levelOrderTraversal(self, root: TreeNode):
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
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res
    def levelOrderTraversal2(self, root: TreeNode):
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
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res[::-1]
    def rightSideView(self, root: TreeNode):
        from collections import deque
        if not root:
            return None
        res = []
        queue = deque()
        queue.append(root)
        while queue:
            levelSize = len(queue)
            for i in range(levelSize):
                node = queue.popleft()
                if i == levelSize -1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res