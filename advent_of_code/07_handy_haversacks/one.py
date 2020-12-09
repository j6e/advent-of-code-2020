import re
from typing import Set

re_main_bag = r"(\w+ \w+) bags contain"
re_contained_bags = r"(\d+) (\w+ \w+)"
my_bag = "shiny gold"


with open('advent_of_code/07_handy_haversacks/input.txt', 'r') as f:
    lines = f.readlines()

rule_bags = {}
for l in lines:
    main_bag = re.findall(re_main_bag, l)[0]
    contained_bags = re.findall(re_contained_bags, l)
    rule_bags[main_bag] = [bag for qty, bag in contained_bags]


def get_container(target_bag: str) -> Set[str]:
    s_bags = set()
    for bag, contained in rule_bags.items():
        if target_bag in contained:
            s_bags.add(bag)
    return s_bags

base = list(get_container('shiny gold'))
i = 0
while i < len(base):
        new = list(get_container(base[i]))
        to_add = [n for n in new if n not in base]
        base += to_add
        i += 1

print(len(base))
