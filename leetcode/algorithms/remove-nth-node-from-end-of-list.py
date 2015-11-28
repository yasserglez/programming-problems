# https://leetcode.com/problems/remove-nth-node-from-end-of-list/


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    current = before_nth = head
    gap = 0
    while current.next is not None:
        current = current.next
        gap += 1
        if gap > n:
            before_nth = before_nth.next
            gap -= 1

    if gap != n:
        return head.next
    else:
        before_nth.next = before_nth.next.next
        return head


def printList(head):
    current = head
    while current is not None:
        if current is not head:
            print(' ', end='')
        print(current.val, end='')
        current = current.next
    print()


if __name__ == '__main__':
    for n in range(1, 6):
        n1 = head = ListNode(1)
        n2 = n1.next = ListNode(2)
        n3 = n2.next = ListNode(3)
        n4 = n3.next = ListNode(4)
        n5 = n4.next = ListNode(5)
        printList(removeNthFromEnd(head, n))
