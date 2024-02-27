class TreeNode:
    def __init__(self, left=None, right=None, val=0):
        self.left = left
        self.right = right
        self.val = val

class Solution:
    def postOrderTraversal(self, root: TreeNode):
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            res.append(node.val)
        return res[::-1]
    def postOrderTraversal2(self, root:TreeNode):
        if not root:
            return []
        left = self.postOrderTraversal(root.left)
        right = self.postOrderTraversal(root.right)
        return left + right + [root.val]        