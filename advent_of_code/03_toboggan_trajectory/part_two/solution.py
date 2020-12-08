with open('advent_of_code/03_toboggan_trajectory/input.txt', 'r') as f:
    lines = [l[:-1] for l in f.readlines()]

length = len(lines)
modulo = len(lines[0])

"""
    Right 1, down 1.
    Right 3, down 1. (This is the slope you already checked.)
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
"""

slopes = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2)
]

multi_counts = 1
for right, down in slopes:
    moduled_indices = [i*right % modulo for i in range(length)]
    counts = [1 if lines[x*down][y] == '#' else 0 for x,y in zip(range(length//down), moduled_indices)]
    print(f'{sum(counts):03} trees encountered in: right {right}, down {down}')
    multi_counts *= sum(counts)

print(multi_counts)