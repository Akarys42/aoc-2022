with open("day_08/input.txt") as file:
    GRID = [[int(t) for t in line.strip()] for line in file.readlines()]

REVERSED_GRID = list(zip(*GRID))
SIZE = len(GRID[0])

visibles = set()
reversed_visibles = set()

for grid, visibles_ in ((GRID, visibles), (REVERSED_GRID, reversed_visibles)):
    for dx, start_pos in ((1, 0), (-1, SIZE - 1)):
        for y, line in enumerate(grid):
            prev_height = -1
            x = start_pos

            while 0 <= x < SIZE:
                if line[x] > prev_height:
                    prev_height = line[x]
                    visibles_.add((x, y))

                x += dx

for y, x in reversed_visibles:
    visibles.add((x, y))

# for y in range(SIZE):
#     for x in range(SIZE):
#         print("X" if (x, y) in visibles else " ", end="")
#     print("")
# print("")

print(len(visibles))
