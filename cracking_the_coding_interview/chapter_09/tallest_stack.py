# Interview Question 9.10

import sys
import itertools


class Box(object):

    def __init__(self, width, height, depth):
        self.width = width
        self.height = height
        self.depth = depth

    def __gt__(self, other):
        return (self.width > other.width and
                self.height > other.height and
                self.depth > other.depth)

    def __lt__(self, other):
        return (self.width < other.width and
                self.height < other.height and
                self.depth < other.depth)

    def __eq__(self, other):
        return not (self < other or self > other)

    def __repr__(self):
        return 'Box({0.width}, {0.height}, {0.depth})'.format(self)


def tallest_stack(boxes):
    # Sort the boxes in decreasing order, build a list of the ordered
    # equivalence classes and pick the tallest box from each class.
    stack = []
    for key, group in itertools.groupby(sorted(boxes, reverse=True)):
        box = max(group, key=lambda box: box.height)
        stack.append(box)
    return stack


if __name__ == '__main__':
    boxes = []
    for line in sys.stdin.readlines():
        dimensions = map(int, line.rstrip().split())
        boxes.append(Box(*dimensions))
    print(sum(box.height for box in tallest_stack(boxes)))
