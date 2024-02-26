class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        res = []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        res = [root.val] + left + right
        return res
    def preorderTraversal2(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return res

        