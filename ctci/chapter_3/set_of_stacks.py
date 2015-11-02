# Interview Question 3.3


class SetOfStacks(object):

    def __init__(self, threshold):
        if threshold <= 0:
            raise ValueError('Invalid threshold value')
        self._threshold = threshold
        self._stacks = []

    def __len__(self):
        return len(self._stacks)

    def push(self, item):
        if not self._stacks or len(self._stacks[-1]) == self._threshold:
            self._stacks.append([])
        self._stacks[-1].append(item)

    def pop(self):
        return self.popAt(-1)

    def popAt(self, index):
        if index >= len(self._stacks) or index < -len(self._stacks):
            raise IndexError('Invalid stack index')
        item = self._stacks[index].pop()
        if not self._stacks[index]:
            del self._stacks[index]
        return item


if __name__ == '__main__':
    s = SetOfStacks(3)
    for item in range(9):
        s.push(item)
    print(len(s))
    while s:
        print(s.pop())
