# Interview Question 3.4

from collections import namedtuple


Tower = namedtuple('Tower', ['name', 'disks'])


def solve(orig, aux, dest):
    num_discs = len(orig.disks)
    _move(num_discs, orig, aux, dest)


def _move(num_discs, orig, aux, dest):
    if num_discs > 0:
        _move(num_discs - 1, orig, dest, aux)
        dest.disks.append(orig.disks.pop())
        if len(dest.disks) > 1:
            assert dest.disks[-1] < dest.disks[-2]
        print('move one disk from {0.name} to {1.name}'.format(orig, dest))
        _move(num_discs - 1, aux, orig, dest)


if __name__ == '__main__':
    tower_a = Tower(name='A', disks=list(range(3, 0, -1)))
    tower_b = Tower(name='B', disks=[])
    tower_c = Tower(name='C', disks=[])
    print(tower_a.disks, tower_b.disks, tower_c.disks)
    solve(tower_a, tower_b, tower_c)
    print(tower_a.disks, tower_b.disks, tower_c.disks)
