from itertools import chain, count
from typing import Iterator

with open("day_14/input.txt") as file:
    WALLS = [
        [[int(num) for num in point.split(",")] for point in line.strip().split(" -> ")]
        for line in file.readlines()
    ]

MIN_X = min(p[0] for p in chain(*WALLS))
MAX_X = max(p[0] for p in chain(*WALLS))
MIN_Y = 0
MAX_Y = max(p[1] for p in chain(*WALLS))

filled_cells = set()


def line(a: int, b: int) -> Iterator[int]:
    step = 1 if b > a else -1

    while a != b:
        yield a
        a += step
    yield b


for wall in WALLS:
    for i in range(1, len(wall)):
        start = wall[i - 1]
        end = wall[i]

        if start[0] == end[0]:
            x = start[0]

            for y in line(start[1], end[1]):
                filled_cells.add((x, y))
        elif start[1] == end[1]:
            y = start[1]

            for x in line(start[0], end[0]):
                filled_cells.add((x, y))
        else:
            raise ValueError


for iteration in count(1):
    sand_x = 500
    sand_y = 0

    while True:
        if sand_y > MAX_Y:
            print(iteration - 1)
            exit()

        if (sand_x, sand_y + 1) not in filled_cells:
            sand_y += 1
        elif (sand_x - 1, sand_y + 1) not in filled_cells:
            sand_x -= 1
            sand_y += 1
        elif (sand_x + 1, sand_y + 1) not in filled_cells:
            sand_x += 1
            sand_y += 1

        else:
            filled_cells.add((sand_x, sand_y))
            break
