# Interview Question 4.7


class Node(object):

    def __init__(self, value):
        self.value = value
        self.parent = Node
        self._left = self._right = None

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        self._left = node
        self._left.parent = self

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        self._right = node
        self._right.parent = self

    def is_ancestor(self, other):
        if self is other:
            return True
        else:
            is_ancestor = False
            if self.left is not None:
                is_ancestor = self.left.is_ancestor(other)
            if not is_ancestor and self.right is not None:
                is_ancestor = self.right.is_ancestor(other)
            return is_ancestor


def first_common_ancestor(node1, node2):
    while node1 is not node2:
        if node1.is_ancestor(node2):
            return node1
        elif node2.is_ancestor(node1):
            return node2
        else:
            assert node1.parent is not None
            assert node2.parent is not None
            node1 = node1.parent
            node2 = node2.parent
    return node1


if __name__ == '__main__':
    n1 = root = Node(1)
    n3 = root.left = Node(3)
    n2 = root.left.right = Node(2)
    n4 = root.right = Node(4)
    n6 = root.right.left = Node(6)
    n5 = root.right.right = Node(5)
    n7 = root.right.right.left = Node(7)

    print(first_common_ancestor(n1, n1).value)
    print(first_common_ancestor(n3, n2).value)
    print(first_common_ancestor(n6, n4).value)
    print(first_common_ancestor(n2, n6).value)
    print(first_common_ancestor(n6, n7).value)
