# Interview Question 4.2

import numpy as np


def dfs(graph, src):
    queue = [src]
    visited = set()    
    while queue:
        i = queue.pop(0)
        yield i
        visited.add(i)
        for j in np.nonzero(graph[i, :])[0]:
            if j not in visited:
                queue.append(j)


def route_between_nodes(graph, n1, n2):
    if graph[n1, n2] or graph[n2, n1]:
        return True
    else:
        for node in dfs(graph, n1):
            if node == n2:
                return True
        for node in dfs(graph, n2):
            if node == n1:
                return True
        return False


if __name__ == '__main__':
    graph = np.array([
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

    for i in range(graph.shape[0]):
        for j in range(graph.shape[1]):
            print(i, j, route_between_nodes(graph, i, j))
