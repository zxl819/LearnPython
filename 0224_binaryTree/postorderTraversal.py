class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode):
        if not root:
            return []
        
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)

        return left + right + [root.val]