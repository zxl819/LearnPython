class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode):
        if not root:
            return []
        stack = []
        result = []
        cur = root
        while cur or stack:
            # 先访问到最底层的左节点
            if cur:
                stack.append(cur)
                cur = cur.left
            # 到达左节点之后处理栈节点
            else:
                cur = stack.pop()
                result.append(cur.val)
                cur = cur.right
        return result


