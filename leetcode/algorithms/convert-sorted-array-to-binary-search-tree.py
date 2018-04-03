# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

import sys


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def sortedArrayToBST(self, nums, start=None, end=None):
        if not nums:
            return None

        if start is None:
            start = 0
        if end is None:
            end = len(nums) - 1

        if start == end:
            root = TreeNode(nums[start])
        elif start + 1 == end:
            root = TreeNode(nums[start])
            root.right = TreeNode(nums[end])
        else:
            middle = (start + end) // 2
            root = TreeNode(nums[middle])
            root.left = self.sortedArrayToBST(nums, start, middle - 1)
            root.right = self.sortedArrayToBST(nums, middle + 1, end)

        return root


def print_inorder(root):

    def collect_inorder(root, values):
        if root:
            collect_inorder(root.left, values)
            values.append(root.val)
            collect_inorder(root.right, values)

    values = []
    collect_inorder(root, values)
    print(' '.join(map(str, values)))


if __name__ == '__main__':
    sol = Solution()
    for line in sys.stdin.readlines():
        values = list(map(int, line.strip().split()))
        root = sol.sortedArrayToBST(values)
        print_inorder(root)
