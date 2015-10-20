# Interview Question 17.6


# Time complexity: O(n^2)
# Auxiliary space complexity: O(n)

def min_unsorted_seq(intergers):
    if not integers:
        return 0, 0
    N = len(integers)
    farthest_less_than = [0] * N
    for i in range(N):
        for j in range(i, N):
            if integers[j] < integers[i]:
                farthest_less_than[i] = j
    m = next((i for i, x in enumerate(farthest_less_than) if x > 0), 0)
    n = max(farthest_less_than)
    if n == 0:
        n = N - 1
    return m, n


if __name__ == '__main__':
    integers = []
    print(min_unsorted_seq(integers))

    integers = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
    print(min_unsorted_seq(integers))

    integers = list(range(13))
    print(min_unsorted_seq(integers))
