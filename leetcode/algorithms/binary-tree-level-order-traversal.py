# https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        results = []
        q = deque([(0, root)])
        while q:
            level, node = q.popleft()
            if len(results) < level + 1:
                results.append([])
            results[level].append(node.val)
            if node.left:
                q.append((level + 1, node.left))
            if node.right:
                q.append((level + 1, node.right))
        return results


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
s = Solution()
r = s.levelOrder(root)
print(r)
