import numpy as np

with open('advent_of_code/01_report_repair/input.txt', 'r') as f:
    numbers = [int(x) for x in f.readlines()]

X = np.array(numbers)
mat_X = np.array([[X]* X.shape[0]]* X.shape[0])
res = mat_X + mat_X.T + mat_X.transpose(1,2,0)
locations = np.where(res == 2020)
a, b, c = X[locations[0][0]], X[locations[1][0]], X[locations[2][0]]
print(f'a: {a}, b: {b}, c: {c}, a+b+c: {a+b+c}, a*b*c: {a*b*c}')
