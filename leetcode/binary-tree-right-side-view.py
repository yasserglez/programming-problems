# https://leetcode.com/problems/binary-tree-right-side-view/

import collections


class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def rightSideView(root):
    view = []
    queue = collections.deque()
    if root is not None:
        queue.append((root, 0))
    while queue:
        node, level = queue.popleft()
        if level == len(view):
            view.append(node.val)
        # Right child goes in first for right-side view
        if node.right is not None:
            queue.append((node.right, level + 1))
        if node.left is not None:
            queue.append((node.left, level + 1))
    return view


if __name__ == '__main__':
    n1 = root = TreeNode(1)
    n2 = n1.left = TreeNode(2)
    n3 = n1.right = TreeNode(3)
    n4 = n3.right = TreeNode(4)
    n5 = n2.right = TreeNode(5)
    n6 = n5.right = TreeNode(6)
    view = rightSideView(root)
    print(' '.join(map(str, view)))
