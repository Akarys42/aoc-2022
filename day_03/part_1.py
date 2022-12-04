import string

with open("day_03/input.txt") as file:
    INPUT = file.readlines()

VALUE = {
    l: i for i, l in enumerate("_" + string.ascii_lowercase + string.ascii_uppercase)
}

total = 0

for compartment in INPUT:
    left = compartment[len(compartment) // 2 :]
    right = compartment[: len(compartment) // 2]

    common_letter = next(iter(set(left) & set(right)))

    total += VALUE[common_letter]

print(total)
