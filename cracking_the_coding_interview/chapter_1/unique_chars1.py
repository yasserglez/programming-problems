import fileinput


# Time complexity: O(n)
# Auxiliary space complexity: O(n)

def unique_chars1(s):
    return len(s) == len(set(s))


if __name__ == '__main__':
    for line in fileinput.input():
        s = line.strip()
        print(int(unique_chars1(s)))
