# https://www.hackerrank.com/challenges/median

import fileinput
import heapq
import collections


class Values(object):

    def __init__(self):
        self._max_heap = []
        self._min_heap = []
        self._values = collections.Counter()

    def __len__(self):
        return len(self._max_heap) + len(self._min_heap)

    def __contains__(self, x):
        return self._values[x] > 0

    def _balance_heaps(self):
        # Balance the heaps if necessary.
        if len(self._max_heap) - len(self._min_heap) > 1:
            y = -heapq.heappop(self._max_heap)
            heapq.heappush(self._min_heap, y)
        if len(self._min_heap) - len(self._max_heap) > 1:
            y = heapq.heappop(self._min_heap)
            heapq.heappush(self._max_heap, -y)

    def add(self, x):
        self._values[x] += 1

        # Add x to the correct heap.
        if not self._max_heap or x <= -self._max_heap[0]:
            heapq.heappush(self._max_heap, -x)
        else:
            heapq.heappush(self._min_heap, x)

        self._balance_heaps()

    def remove(self, x):
        self._values[x] -= 1

        # Remove the element and restore the heap property.
        if x <= -self._max_heap[0]:
            self._max_heap.remove(-x)
            heapq.heapify(self._max_heap)
        else:
            self._min_heap.remove(x)
            heapq.heapify(self._min_heap)

        self._balance_heaps()

    def get_median(self):
        if len(self._max_heap) > len(self._min_heap):
            return -self._max_heap[0]
        elif len(self._min_heap) > len(self._max_heap):
            return self._min_heap[0]
        else:
            x = -self._max_heap[0]
            y = self._min_heap[0]
            return (x + y) / 2


def format_median(median):
    return ('%f' % median).rstrip('0').rstrip('.')


if __name__ == '__main__':
    values = Values()
    with fileinput.input() as fi:
        N = int(fi.readline())
        for n in range(N):
            op, x = fi.readline().strip().split()
            x = int(x)
            if op == 'a':
                values.add(x)
                print(format_median(values.get_median()))
            elif op == 'r':
                if x in values:
                    values.remove(x)
                    if values:
                        print(format_median(values.get_median()))
                    else:
                        print('Wrong!')
                else:
                    print('Wrong!')
