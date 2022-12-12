import string
from dataclasses import dataclass
from math import sqrt
from queue import PriorityQueue
from typing import Optional, Iterator


@dataclass
class Node:
    x: int
    y: int
    height: int
    gscore: int = float("inf")
    previous_path: Optional["Node"] = None

    def __hash__(self) -> int:
        return hash(hash(self.x) + hash(self.y))

    def __eq__(self, other: "Node") -> bool:
        return self.x == other.x and self.y == other.y

    # We need a bogus sort method so the priority queue doesn't get confused
    def __lt__(self, other: "Node") -> bool:
        return (self.x, self.y) < (other.x, other.y)

    @property
    def neighbors(self) -> Iterator["Node"]:
        for dx, dy in NEIGHBORS:
            x = self.x + dx
            y = self.y + dy
            if (0 <= x < SIZE_X) and (0 <= y < SIZE_Y):
                if GRID[y][x].height - self.height <= 1:
                    yield GRID[y][x]


HEIGHT_MAPPING = {l: i for i, l in enumerate(string.ascii_lowercase)}
START = None
END = None
NEIGHBORS = ((-1, 0), (1, 0), (0, -1), (0, 1))

GRID = []

with open("day_12/input.txt") as file:
    for y, line in enumerate(file.readlines()):
        line_content = []

        for x, c in enumerate(line.strip()):

            if c == "S":
                node = Node(x, y, HEIGHT_MAPPING["a"])
                START = node
            elif c == "E":
                node = Node(x, y, HEIGHT_MAPPING["z"])
                END = node
            else:
                node = Node(x, y, HEIGHT_MAPPING[c])
            line_content.append(node)

        GRID.append(line_content)

SIZE_X = len(GRID[0])
SIZE_Y = len(GRID)


def h(node: Node) -> float:
    return sqrt((node.x - END.x) ** 2 + (node.y - END.y) ** 2)


START.gscore = 0

open_set = PriorityQueue()
open_set.put((h(START), START))

open_set_content = {START}

while not open_set.empty():
    _, current = open_set.get()
    current: Node
    open_set_content.remove(current)

    new_gscore = current.gscore + 1

    for neighbor in current.neighbors:

        if neighbor == END:
            print(new_gscore)
            exit()

        if new_gscore < neighbor.gscore:
            neighbor.previous_path = current
            neighbor.gscore = new_gscore

            if neighbor not in open_set_content:
                open_set.put((new_gscore + h(neighbor), neighbor))
                open_set_content.add(neighbor)
assert False
