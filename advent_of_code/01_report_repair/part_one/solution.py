import numpy as np

with open('advent_of_code/01_report_repair/input.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]

X = np.array(numbers)
mat_X = np.matrix([X]* X.shape[0])
res = mat_X + mat_X.T
locations = np.where(res == 2020)
a, b = X[locations[0][0]], X[locations[0][1]]
print(f'a: {a}, b: {b}, a+b: {a+b}, a*b: {a*b}')
