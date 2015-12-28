# https://www.hackerrank.com/challenges/time-conversion

import re
import sys


def convert_time(time):
    match = re.match(r'(?P<h>\d+):(?P<m>\d+):(?P<s>\d+)(AM|PM)', time)
    h = int(match.group('h'))
    m = int(match.group('m'))
    s = int(match.group('s'))
    if h == 12:
        if time.endswith('AM'):
            h = 0
    elif time.endswith('PM'):
        h += 12
    return '{h:02}:{m:02}:{s:02}'.format(h=h, m=m, s=s)


if __name__ == '__main__':
    for line in sys.stdin:
        time = line.strip()
        print(convert_time(time))
