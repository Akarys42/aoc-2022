with open("day_01/input.txt") as file:
    INPUT = [map(int, chunk.split("\n")) for chunk in file.read().split("\n\n")]

print(max(sum(chunk) for chunk in INPUT))
