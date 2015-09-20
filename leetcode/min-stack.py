# https://leetcode.com/problems/min-stack/
#
# Time complexity: O(1)
# Auxiliary space complexity: O(n)


class MinStackError(Exception):
    pass


class MinStack(object):

    def __init__(self):
        self._stack = []

    def push(self, x):
        try:
            current_min = min(x, self.getMin())
        except MinStackError:
            current_min = x
        self._stack.append((x, current_min))

    def pop(self):
        if not self._stack:
            raise MinStackError()
        self._stack.pop()

    def top(self):
        if not self._stack:
            raise MinStackError()
        return self._stack[-1][0]

    def getMin(self):
        if not self._stack:
            raise MinStackError()
        return self._stack[-1][1]


if __name__ == '__main__':
    s = MinStack()

    s.push(3)
    print(s.top(), s.getMin())
    s.push(2)
    print(s.top(), s.getMin())
    s.push(4)
    print(s.top(), s.getMin())
    s.push(2)
    print(s.top(), s.getMin())
    s.push(1)
    print(s.top(), s.getMin())

    s.pop()
    print(s.top(), s.getMin())
    s.pop()
    print(s.top(), s.getMin())
    s.pop()
    print(s.top(), s.getMin())
    s.pop()
    print(s.top(), s.getMin())
    s.pop()
