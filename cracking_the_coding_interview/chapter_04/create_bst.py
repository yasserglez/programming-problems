# Interview Question 4.3


class BST(object):

    def __init__(self, value):
        self.value = value
        self.left = self.right = None

    def compute_height(self):
        height_left = 0 if self.left is None else self.left.compute_height()
        height_right = 0 if self.right is None else self.right.compute_height()
        return max(height_left, height_right) + 1


# Time complexity: O(n)
# Auxiliary space complexity: O(n)

def create_bst(numbers):
    n = len(numbers)
    if n == 0:
        return None
    else:
        i = n // 2
        node = BST(numbers[i])
        node.left = create_bst(numbers[:i])
        node.right = create_bst(numbers[i+1:])
        return node


if __name__ == '__main__':
    numbers = [2, 4, 5, 7, 9, 15, 21]
    tree = create_bst(numbers)
    print(tree.compute_height())
