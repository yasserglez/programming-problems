# Interview Question 2.1


class ListNode(object):

    def __init__(self, value):
        self.value = value
        self.next = None


def remove_suplicates(head):
    values = set()
    prev = None
    curr = head
    while curr is not None:
        if curr.value in values:
            prev.next = curr.next
        else:
            values.add(curr.value)
            prev = curr
        curr = curr.next


if __name__ == '__main__':
    n1a = head = ListNode(1)
    n2a = n1a.next = ListNode(2)
    n1b = n2a.next = ListNode(1)
    n1c = n1b.next = ListNode(1)
    n3 = n1c.next = ListNode(3)
    n2b = n3.next = ListNode(2)

    remove_suplicates(head)

    values = []
    curr = head
    while curr is not None:
        values.append(curr.value)
        curr = curr.next
    print(' '.join(map(str, values)))
