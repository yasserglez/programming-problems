# Interview Question 17.12


# Time complexity: O(n)
# Auxiliary space complexity: O(n)

def same_sum_pairs(numbers, sum_value):
    pairs = []
    complements = set()
    for n in numbers:
        n_complement = sum_value - n
        if n_complement in complements:
            pairs.append((n_complement, n))
        complements.add(n)
    return pairs


if __name__ == '__main__':
    numbers = [2, 4, 2, 3, 1, 0]
    pairs = same_sum_pairs(numbers, 4)
    for pair in pairs:
        print(*pair)
