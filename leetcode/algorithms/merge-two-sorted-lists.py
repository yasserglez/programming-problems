# https://leetcode.com/problems/merge-two-sorted-lists/

import sys


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def mergeTwoLists(self, l1, l2):
        
        head = last = None

        def append(node):
            nonlocal head, last
            if not head:
                head = last = node
            else:
                last.next = node
                last = node

        while l1 or l2:
            if l1 and l2:
                if l1.val < l2.val:
                    append(l1)
                    l1 = l1.next
                else:
                    append(l2)
                    l2 = l2.next
            elif l1:
                append(l1)
                l1 = l1.next
            else:
                append(l2)
                l2 = l2.next

        return head


def read_list():
    values = list(map(int, sys.stdin.readline().strip().split()))
    head = last = None
    for val in values:
        if not last:
            head = last = ListNode(val)
        else:
            last.next = ListNode(val)
            last = last.next
    return head


def print_list(l):
    ptr = l
    values = []
    while ptr:
        values.append(ptr.val)
        ptr = ptr.next
    print(' '.join(map(str, values)))


if __name__ == '__main__':
    sol = Solution()
    num_problems = int(sys.stdin.readline())
    for _ in range(num_problems):
        l1, l2 = read_list(), read_list()
        res = sol.mergeTwoLists(l1, l2)
        print_list(res)
