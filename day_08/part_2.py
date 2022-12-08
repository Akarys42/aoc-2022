from itertools import permutations

with open("day_08/input.txt") as file:
    GRID = [[int(t) for t in line.strip()] for line in file.readlines()]

DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))
SIZE = len(GRID[0])

best_score = -1

for start_x, start_y in permutations(range(SIZE), 2):
    total_score = 1

    max_length = GRID[start_y][start_x]

    for dx, dy in DIRECTIONS:
        x = start_x
        y = start_y

        in_view = 0

        while True:
            x += dx
            y += dy

            if not (0 <= x < SIZE) or not (0 <= y < SIZE):
                break

            in_view += 1

            if GRID[y][x] >= max_length:
                break

        total_score *= in_view

    if total_score > best_score:
        best_score = total_score

print(best_score)
