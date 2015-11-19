# https://www.hackerrank.com/challenges/botcleanlarge

import sys
import collections


def get_move(grid, bot):
    # Build the graph
    height, width = len(grid), len(grid[0])
    graph = {}
    for i in range(height):
        for j in range(width):
            v = i, j
            graph[v] = collections.OrderedDict()
            if i != 0:
                graph[v]['UP'] = (i - 1, j)
            if i != height - 1:
                graph[v]['DOWN'] = (i + 1, j)
            if j != 0:
                graph[v]['LEFT'] = (i, j - 1)
            if j != width - 1:
                graph[v]['RIGHT'] = (i, j + 1)
    # Breath-first search
    v = bot
    queue = collections.deque([v])
    path = {v: None}
    while grid[v[0]][v[1]] != 'd':
        v = queue.popleft()
        for move, w in graph[v].items():
            if w not in path:
                path[w] = (v, move)
                queue.append(w)
    # Return a move that leads to the closest dirty square
    v, move = path[v]
    while v != bot:
        v, move = path[v]
    return move


def get_action(grid, i, j):
    return 'CLEAN' if grid[i][j] == 'd' else get_move(grid, (i, j))


if __name__ == '__main__':
    f = sys.stdin
    i, j = tuple(map(int, f.readline().rstrip().split()))
    height, width = tuple(map(int, f.readline().rstrip().split()))
    grid = []
    for k in range(height):
        grid.append(f.readline().rstrip())
    print(get_action(grid, i, j))
