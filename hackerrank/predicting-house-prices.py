# https://www.hackerrank.com/challenges/predicting-house-prices

import sys

import numpy as np
from sklearn.linear_model import LinearRegression


if __name__ == '__main__':
    f = sys.stdin
    # Load the training data
    F, N = map(int, f.readline().rstrip().split())
    X, y = np.zeros((N, F)), np.zeros(N)
    for i in range(N):
        values = list(map(float, f.readline().rstrip().split()))
        X[i, :], y[i] = values[:F], values[F]
    # Build the linear model
    model = LinearRegression()
    model.fit(X, y)
    # Predict the house prices
    T = int(f.readline())
    for i in range(T):
        values = list(map(float, f.readline().rstrip().split()))
        x = np.asarray(values).reshape(1, -1)
        print('%.2f' % round(float(model.predict(x)), 2))
