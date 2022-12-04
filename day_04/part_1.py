with open("day_04/input.txt") as file:
    INPUT = file.readlines()

total = 0

for line in INPUT:
    left_pair, right_pair = line.strip().split(",")

    l1, l2 = left_pair.split("-")
    left_range = set(range(int(l1), int(l2) + 1))

    r1, r2 = right_pair.split("-")
    right_range = set(range(int(r1), int(r2) + 1))

    if len(left_range - right_range) == 0 or len(right_range - left_range) == 0:
        total += 1

print(total)
