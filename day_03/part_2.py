import string
from functools import reduce
from operator import and_

with open("day_03/input.txt") as file:
    INPUT = [l.strip() for l in file.readlines()]

VALUE = {
    l: i for i, l in enumerate("_" + string.ascii_lowercase + string.ascii_uppercase)
}

total = 0

for i in range(len(INPUT) // 3):
    group = INPUT[i * 3 : (i + 1) * 3]

    common_values = reduce(and_, (set(bag) for bag in group))

    total += VALUE[next(iter(common_values))]

print(total)
