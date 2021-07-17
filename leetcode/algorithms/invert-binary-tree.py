# https://leetcode.com/problems/invert-binary-tree/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.right, root.left = self.invertTree(root.left), self.invertTree(root.right)
        return root


root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)
s = Solution()
new_root = s.invertTree(root)
print([new_root.val, new_root.left.val, new_root.right.val])
