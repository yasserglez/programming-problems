# https://www.hackerrank.com/challenges/median

import fileinput
import heapq
import collections


class Values(object):

    def __init__(self):
        self._values = collections.Counter()
        self._max_heap = []
        self._max_heap_count = 0
        self._max_heap_bl = collections.Counter()
        self._min_heap = []
        self._min_heap_count = 0
        self._min_heap_bl = collections.Counter()

    def __len__(self):
        return self._max_heap_count + self._min_heap_count

    def __contains__(self, x):
        return self._values[x] > 0

    def _update_heaps(self):
        self._cleanup_heaps()
        self._balance_heaps()
        self._cleanup_heaps()

    def _balance_heaps(self):
        # Balance the heaps if necessary.

        if self._max_heap_count - self._min_heap_count > 1:
            x = -heapq.heappop(self._max_heap)
            self._max_heap_count -= 1
            heapq.heappush(self._min_heap, x)
            self._min_heap_count += 1

        if self._min_heap_count - self._max_heap_count > 1:
            x = heapq.heappop(self._min_heap)
            self._min_heap_count -= 1
            heapq.heappush(self._max_heap, -x)
            self._max_heap_count += 1

    def _cleanup_heaps(self):
        # Ensure that the top element of each heap is not blacklisted.
        self._cleanup_heap(self._max_heap, self._max_heap_bl)
        self._cleanup_heap(self._min_heap, self._min_heap_bl)

    def _cleanup_heap(self, heap, heap_bl):
        while heap and heap_bl[heap[0]] > 0:
            x = heapq.heappop(heap)
            heap_bl[x] -= 1
            if heap_bl[x] == 0:
                del heap_bl[x]

    def add(self, x):
        self._values[x] += 1

        # Add x to the correct heap.
        if not self._max_heap or x <= -self._max_heap[0]:
            heapq.heappush(self._max_heap, -x)
            self._max_heap_count += 1
        else:
            heapq.heappush(self._min_heap, x)
            self._min_heap_count += 1

        self._update_heaps()

    def remove(self, x):
        self._values[x] -= 1
        if self._values[x] == 0:
            del self._values[x]

        # Add the element to the blacklist.
        if x <= -self._max_heap[0]:
            self._max_heap_bl[-x] += 1
            self._max_heap_count -= 1
        else:
            self._min_heap_bl[x] += 1
            self._min_heap_count -= 1

        self._update_heaps()

    def get_median(self):
        if self._max_heap_count > self._min_heap_count:
            return -self._max_heap[0]
        elif self._min_heap_count > self._max_heap_count:
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
