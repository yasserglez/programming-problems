# Interview Question 1.1

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
    print(unique_chars2(""))
    print(unique_chars2("a"))
    print(unique_chars2("aa"))
    print(unique_chars2("abc"))
    print(unique_chars2("abca"))
    print(unique_chars2("abcb"))
    print(unique_chars2("abcc"))
