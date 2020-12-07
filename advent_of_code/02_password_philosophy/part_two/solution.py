import re
from collections import Counter

regex = r"(\d+)-(\d+) (\w): (\w+)"
with open('advent_of_code/02_password_philosophy/input.txt', 'r') as f:
    lines = ''.join(f.readlines())

matches = re.findall(regex, lines, re.MULTILINE)
correct = 0
for pos_one, pos_two, letter, password in matches:
    pos_one, pos_two = int(pos_one) - 1, int(pos_two) - 1 # not zero indexed
    
    if len(password) < max(pos_one, pos_two): 
        continue
    
    if (password[pos_one] == letter) != (password[pos_two] == letter): # XOR
        correct += 1

print(f'{correct} valid passwords')
