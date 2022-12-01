with open("day_01/input.txt") as file:
    INPUT = [map(int, chunk.split("\n")) for chunk in file.read().split("\n\n")]

totals = [sum(chunk) for chunk in INPUT]
totals.sort()

print(sum(totals[-3:]))
