from typing import List
from collections import Counter
from functools import reduce


def parse_blocks(text: str) -> List[List[str]]:
    res = [block.split('\n') for block in text.split('\n\n')]
    return res


def get_all_yes(group: str) -> int:
    group = [m for m in group if m != '']
    intersection = reduce(lambda a, b: set(a) & set(b), group)
    n = len(intersection)
    print(n, group, intersection)
    return n


if __name__ == "__main__":
    with open('advent_of_code/06_custom_customs/input.txt', 'r') as f:
        input = ''.join(f.readlines())
    blocks = parse_blocks(input)
    ans = [get_all_yes(group) for group in blocks]
    print()
    print(sum(ans))
