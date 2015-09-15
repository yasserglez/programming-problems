import fileinput


# Time complexity: O(n^2)
# Auxiliary space complexity: O(1)

def unique_chars2(s):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                return False
    return True


if __name__ == '__main__':
    for line in fileinput.input():
        s = line.strip()
        print(int(unique_chars2(s)))
