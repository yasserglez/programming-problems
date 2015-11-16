# Interview Question 11.5


def find_location(s, strings):
    return _bisect(strings, s, 0, len(strings))


def _bisect(strings, s, start, end):
    if start > end:
        return -1
    else:
        middle = (end - start) // 2
        if not strings[middle]:
            index = _bisect(strings, s, start, end - 1)
            if index > 0:
                return index
            else:
                return _bisect(strings, s, start + 1, end)
        elif s == strings[middle]:
            return middle
        elif s < strings[middle]:
            return _bisect(strings, s, start, middle)
        else:
            return _bisect(strings, s, middle, end)


if __name__ == '__main__':
    strings = ["at", "", "", "", "ball", "", "", "car", "", "", "dad", "", ""]
    print(find_location("ball", strings))
