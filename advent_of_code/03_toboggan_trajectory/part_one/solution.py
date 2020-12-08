with open('advent_of_code/03_toboggan_trajectory/input.txt', 'r') as f:
    lines = [l[:-1] for l in f.readlines()]

length = len(lines)
indices = [i*3 for i in range(length)]
modulo = len(lines[0])
moduled_indices = [i % modulo for i in indices]

counts = [1 if lines[x][y] == '#' else 0 for x, y in zip(range(length), moduled_indices) ]

# for x,y in zip(range(length), moduled_indices):
#    print(f'{lines[x][y]} - {y} - {lines[x]}')

print(f'{sum(counts)} trees encountered')