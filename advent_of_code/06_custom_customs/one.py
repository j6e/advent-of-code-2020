from typing import List


def parse_blocks(text: str) -> List[str]:
    res = [block.replace('\n', '') for block in text.split('\n\n')]
    return res


def get_unique_answers(group_answers: str) -> int:
    unique = set(group_answers)
    n = len(unique)
    print(group_answers, unique, n )
    return n


if __name__ == "__main__":
    with open('advent_of_code/06_custom_customs/input.txt', 'r') as f:
        input = ''.join(f.readlines())
    blocks = parse_blocks(input)
    ans = [get_unique_answers(group) for group in blocks]
    print(ans)
    print(sum(ans))    