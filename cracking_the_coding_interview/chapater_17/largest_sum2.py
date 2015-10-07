# Interview Question 17.8


# Time complexity: O(n)
# Auxiliary space complexity: O(1)

def largest_sum(numbers):
    max_sum = 0
    curr_sum = 0
    for x in numbers:
        # Only makes sense to include it if we're better off with it,
        # otherwise the empty sequence is better.
        curr_sum += x
        if curr_sum < 0:
            curr_sum = 0
        # Update the maximum sum, if it changed.
        if curr_sum > max_sum:
            max_sum = curr_sum
    return max_sum


if __name__ == '__main__':
    numbers = [2, -8, 3, -2, 4, -10]
    print(largest_sum(numbers))

    numbers = [1, 2, 3, 4, 5]
    print(largest_sum(numbers))

    numbers = [-1, -2, -3, -4, -5]
    print(largest_sum(numbers))
