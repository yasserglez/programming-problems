# Interview Question 17.6


# Time complexity: O(n)
# Auxiliary space complexity: O(1)

def min_unsorted_seq(intergers):
    if not integers:
        return 0, 0

    N = len(integers)

    left_ends = N - 1
    for i in range(1, N):
        if integers[i - 1] > integers[i]:
            left_ends = i - 1
            break

    right_begins = 0
    for i in range(N - 1, 1, -1):
        if integers[i - 1] > integers[i]:
            right_begins = i
            break

    m, n = 0, N - 1
    if right_begins != 0:
        min_middle = min(integers[left_ends + 1:right_begins + 1])
        for i in range(left_ends, 1, -1):
            if integers[i] <= min_middle:
                m = i + 1
                break
        max_middle = max(integers[left_ends + 1:right_begins + 1])
        for i in range(right_begins, N):
            if integers[i] >= max_middle:
                n = i - 1
                break

    return m, n


if __name__ == '__main__':
    integers = []
    print(min_unsorted_seq(integers))

    integers = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print(min_unsorted_seq(integers))

    integers = list(range(13))
    print(min_unsorted_seq(integers))
