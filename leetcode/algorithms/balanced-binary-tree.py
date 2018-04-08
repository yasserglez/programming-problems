# https://leetcode.com/problems/balanced-binary-tree/


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def _isBlanced(self, root):
        if root is None:
            return (True, 0)
        else:
            left = self._isBlanced(root.left)
            if not left[0]:
                return (False, )
            right = self._isBlanced(root.right)
            if not right[0]:
                return (False, )
            if abs(left[1] - right[1]) > 1:
                return (False, )
            else:
                height = 1 + max(left[1], right[1])
                return (True, height)


    def isBalanced(self, root):
        return self._isBlanced(root)[0]


if __name__ == '__main__':
    sol = Solution()

    # Example 1
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)
    print(sol.isBalanced(tree))

    # Example 2
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(2)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(3)
    tree.left.left.left = TreeNode(4)
    tree.left.left.right = TreeNode(4)
    print(sol.isBalanced(tree))
