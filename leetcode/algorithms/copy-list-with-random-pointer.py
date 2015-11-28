# https://leetcode.com/problems/copy-list-with-random-pointer/

import fileinput
import re


class RandomListNode(object):

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):

    def copyRandomList(self, head):
        node_map = {}  # Maps the original nodes to the copies.

        new_head = None
        if head is not None:
            # Copy the head of the list.
            new_head = RandomListNode(head.label)
            node_map[id(head)] = new_head

            # Copy the rest of the list.
            curr = head.next
            new_curr = new_head
            while curr is not None:
                new_curr.next = RandomListNode(curr.label)
                node_map[id(curr)] = new_curr.next
                curr = curr.next
                new_curr = new_curr.next

        # Update the random attribute.
        curr, new_curr = head, new_head
        while new_curr is not None:
            if curr.random:
                new_curr.random = node_map[id(curr.random)]
            curr, new_curr = curr.next, new_curr.next

        return new_head

    def printRandomList(self, head):
        nodes = []
        curr = head
        while curr is not None:
            random = 'null' if curr.random is None else curr.random.label
            node = '{label}({random})'.format(label=curr.label, random=random)
            nodes.append(node)
            curr = curr.next
        print(' '.join(nodes))


if __name__ == '__main__':
    # Test case format does not support multiple nodes with the same label.
    s = Solution()
    for line in fileinput.input():
        nodes = {'null': None}
        head = prev = None
        for node in line.rstrip().split():
            match = re.match(r'([^)]+)\(([^)]+)\)', node)
            label, random = match.groups()
            curr = nodes[label] = RandomListNode(label)
            curr.random = random
            if prev is None:
                head = curr
            else:
                prev.next = curr
            prev = curr
        curr = head
        while curr is not None:
            curr.random = nodes[curr.random]
            curr = curr.next
        new_head = s.copyRandomList(head)
        s.printRandomList(new_head)
