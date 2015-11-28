# https://www.hackerrank.com/challenges/saveprincess

import sys
import collections


def displayPathtoPrincess(n, grid):
    m = p = None
    # Build the graph
    graph = {}
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                m = (i, j)
            if grid[i][j] == 'p':
                p = (i, j)
            v = (i, j)
            graph[v] = collections.OrderedDict()
            if i != 0:
                graph[v]['UP'] = (i - 1, j)
            if i != n - 1:
                graph[v]['DOWN'] = (i + 1, j)
            if j != 0:
                graph[v]['LEFT'] = (i, j - 1)
            if j != n - 1:
                graph[v]['RIGHT'] = (i, j + 1)
    # Breath-first search
    v = m
    queue = collections.deque([v])
    path = {v: None}
    while v != p:
        v = queue.popleft()
        for move, w in graph[v].items():
            if w not in path:
                path[w] = (v, move)
                queue.append(w)
    # Print the optimal moves
    v, move = path[p]
    moves = [move]
    while v != m:
        v, move = path[v]
        moves.append(move)
    for move in reversed(moves):
        print(move)


if __name__ == '__main__':
    f = sys.stdin
    n = int(f.readline())
    grid = []
    for i in range(n):
        grid.append(f.readline().rstrip())
    displayPathtoPrincess(n, grid)
