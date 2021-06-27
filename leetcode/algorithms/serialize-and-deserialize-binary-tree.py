# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

import json
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        data = []
        node_queue = deque([root])
        while node_queue:
            node = node_queue.popleft()
            data.append(node.val if node else None)
            if node:
                node_queue.append(node.left)
                node_queue.append(node.right)
        return json.dumps(data)

    def deserialize(self, data):
        data = json.loads(data)
        i = 0
        root = TreeNode(data[i]) if data[i] is not None else None
        node_queue = deque([root])
        while node_queue:
            node = node_queue.popleft()
            if node:
                if 2 * i + 1 < len(data) and data[2 * i + 1] is not None:
                    node.left = TreeNode(data[2 * i + 1])
                    node_queue.append(node.left)
                if 2 * i + 2 < len(data) and data[2 * i + 2] is not None:
                    node.right = TreeNode(data[2 * i + 2])
                    node_queue.append(node.right)
            i += 1
        return root


root = None
print(Codec().serialize(root))

root = TreeNode(1)
print(Codec().serialize(root))

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(5)
print(Codec().serialize(root))

root = x = TreeNode(1)
for i in range(2, 101):
    x.right = TreeNode(i)
    x = x.right
print(Codec().serialize(root))
