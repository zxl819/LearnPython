class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                res.append(cur.val)
                cur = cur.right
        return res
    def inorderTraversal2(self, root: TreeNode):
        if not root:
            return []
        left = self.inorderTraversal2(root.left)
        right = self.inorderTraversal2(root.right)
        return left + [root.val] + right
