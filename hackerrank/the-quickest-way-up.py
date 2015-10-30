# https://www.hackerrank.com/challenges/the-quickest-way-up

import sys
import collections


def _build_graph(snakes, ladders):
    snakes_dict = {(s0 - 1): (s1 - 1) for s0, s1 in snakes}
    ladders_dict = {(l0 - 1): (l1 - 1) for l0, l1 in ladders}
    graph = [[] for _ in range(100)]
    for i in range(100):
        for dice_roll in range(1, 7):
            j = i + dice_roll
            if j in snakes_dict:
                j = snakes_dict[j]
            elif j in ladders_dict:
                j = ladders_dict[j]
            if j <= 99:
                graph[i].append(j)
    return graph


# Breadth-first search
def _min_number_of_moves(graph):
    queue = collections.deque([0])
    distance = [0] + [-1] * 99
    while queue:
        i = queue.popleft()
        for j in graph[i]:
            if distance[j] == -1:
                if j == 99:
                    return distance[i] + 1
                distance[j] = distance[i] + 1
                queue.append(j)
    return -1


def quickest_way_up(snakes, ladders):
    graph = _build_graph(snakes, ladders)
    return _min_number_of_moves(graph)


if __name__ == '__main__':
    f = sys.stdin
    T = int(f.readline().rstrip())
    for t in range(T):
        snakes, ladders = [], []
        num_snakes = int(f.readline().rstrip())
        for i in range(num_snakes):
            snakes.append(tuple(map(int, f.readline().rstrip().split())))
        num_ladders = int(f.readline().rstrip())
        for i in range(num_ladders):
            ladders.append(tuple(map(int, f.readline().rstrip().split())))
        print(quickest_way_up(snakes, ladders))
