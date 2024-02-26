# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        resleft = 1
        stack = []
        cur = root
        while cur or stack:
            if cur:
               stack.append(cur)
               cur = cur.left
               resleft += 1
            else:
                cur = stack.pop()
                resright = resleft - 1
                while cur:
                    cur = cur.right
                    resright += 1
        return resleft


def insertLevelOrder(arr, root, i, n):
    if i < n:
        tmp = TreeNode(arr[i])
        root = tmp 
        root.left = insertLevelOrder(arr, root.left, 2 * i + 1, n)
        root.right = insertLevelOrder(arr, root.right, 2 * i + 2, n)
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val, end = ' ')
        inOrder(root.right)

if __name__ == '__main__':
    arr = [3,9,20,None, None,15,7]
    n = len(arr)
    root = None
    root = insertLevelOrder(arr, root, 0, n)
    print(Solution().minDepth(root))
