# Interview Question 17.8


# Time complexity: O(n^2)
# Auxiliary space complexity: O(1)

def largest_sum(numbers):
    max_sum = None
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            curr_sum = sum(numbers[i:j+1])
            if max_sum is None or curr_sum > max_sum:
                max_sum = curr_sum
    return max(0, max_sum)


if __name__ == '__main__':
    numbers = [2, -8, 3, -2, 4, -10]
    print(largest_sum(numbers))

    numbers = [1, 2, 3, 4, 5]
    print(largest_sum(numbers))

    numbers = [-1, -2, -3, -4, -5]
    print(largest_sum(numbers))
