# Interview Question 7.3

import sys

class Line(object):

    def __init__(self, slope, intercept):
        self.slope = slope
        self.intercept = intercept

    def intersects(self, other, eps=1e-6):
        return (abs(self.slope - other.slope) > eps or 
                abs(self.intercept - other.intercept) <= eps)
            

if __name__ == '__main__':
    f = sys.stdin
    num_problems = int(f.readline())
    for _ in range(num_problems):
        line1 = Line(*list(map(float, f.readline().split())))
        line2 = Line(*list(map(float, f.readline().split())))
        print(line1.intersects(line2))
