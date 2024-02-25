class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        left = self.preorderTraversal(root.left)
        right = self.preorderTraversal(root.right)
        return [root.val] + left + right
    
    def inorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        left = self.inorderTraversal(root.left)
        right = self.inorderTraversal(root.right)

        return left + [root.val] + right
    
    def postinorderTraversal(self, root: TreeNode) -> list[int]:
        if not root:
            return []
        left = self.postinorderTraversal(root.left)
        right = self.postinorderTraversal(root.right)

        return left + right + [root.val]
