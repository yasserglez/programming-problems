# Interview Question 3.4


def recursive_solution(num_discs, tower1, tower2, tower3):
    _move(num_discs, tower1, tower3, tower2)


def _move(num_discs, orig, dest, aux):
    if num_discs > 0:
        _move(num_discs - 1, orig, aux, dest)
        print('move one disk from {0} to {1}'.format(orig, dest))
        _move(num_discs - 1, aux, dest, orig)


def iterative_solution(num_discs, tower1, tower2, tower3):
    stack = []
    stack.append((num_discs, tower1, tower3, tower2))
    while stack:
        item = stack.pop()
        if len(item) == 2:
            print('move one disk from {0} to {1}'.format(*item))
        else:
            k, orig, dest, aux = item
            if k > 0:
                stack.append((k - 1, aux, dest, orig))
                stack.append((orig, dest))
                stack.append((k - 1, orig, aux, dest))


if __name__ == '__main__':
    iterative_solution(5, 'A', 'B', 'C')
