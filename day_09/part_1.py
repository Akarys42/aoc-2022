from itertools import product


def add_coords(a: tuple[int, int], b: tuple[int, int]) -> tuple[int, int]:
    return a[0] + b[0], a[1] + b[1]


def distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def axis_distance(a: tuple[int, int], b: tuple[int, int]) -> int:
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))


with open("day_09/input.txt") as file:
    INSTRUCTIONS = [line.strip().split(" ") for line in file.readlines()]

DIRECTIONS = {"L": (-1, 0), "U": (0, 1), "R": (1, 0), "D": (0, -1)}
MOVES = list(product((-1, 0, 1), repeat=2))

visited = {(0, 0)}

head = (0, 0)
tail = (0, 0)

for direction_id, steps in INSTRUCTIONS:
    direction = DIRECTIONS[direction_id]

    for _ in range(int(steps)):
        head = add_coords(head, direction)

        if axis_distance(head, tail) <= 1:
            continue

        possible_moves = []

        for possible_move in MOVES:
            new_tail = add_coords(tail, possible_move)
            possible_moves.append((distance(new_tail, head), possible_move))

        possible_moves.sort()
        best_move = possible_moves[0][1]

        tail = add_coords(tail, best_move)
        visited.add(tail)

print(len(visited))
