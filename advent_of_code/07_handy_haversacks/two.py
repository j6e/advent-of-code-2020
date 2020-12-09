import re
from typing import List

re_main_bag = r"(\w+ \w+) bags contain"
re_contained_bags = r"(\d+) (\w+ \w+)"
my_bag = "shiny gold"


with open('advent_of_code/07_handy_haversacks/input.txt', 'r') as f:
    lines = f.readlines()

rule_bags = {}
for l in lines:
    main_bag = re.findall(re_main_bag, l)[0]
    contained_bags = re.findall(re_contained_bags, l)
    rule_bags[main_bag] = {bag: int(qty) for qty, bag in contained_bags}


def get_inside(target_bag: str) -> int:
    if not rule_bags[target_bag]:
        return 1, 0
    else:
        accu = 0
        for bag, qty in rule_bags[target_bag].items():
            v, b = get_inside(bag)
            accu += qty * v + qty * b
        return accu, 1


res, _ = get_inside(my_bag)
print(f'{res} bags inside my bag')

