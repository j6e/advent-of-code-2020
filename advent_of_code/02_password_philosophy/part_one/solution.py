import re
from collections import Counter

regex = r"(\d+)-(\d+) (\w): (\w+)"
with open('advent_of_code/02_password_philosophy/input.txt', 'r') as f:
    lines = ''.join(f.readlines())

matches = re.findall(regex, lines, re.MULTILINE)
correct = 0
for mini, maxi, letter, password in matches:
    mini, maxi = int(mini), int(maxi)
    counter = Counter(password)
    if letter in counter.keys() and (counter[letter] <= maxi and counter[letter] >= mini):
        correct += 1

print(f'{correct} valid passwords')
