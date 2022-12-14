from itertools import zip_longest
from functools import cmp_to_key
import ast

with open("day_13/input.txt") as file:
    PACKETS = [
        ast.literal_eval(line.strip()) for line in file.readlines() if len(line) > 1
    ]

PairTyping = int | list["PairTyping"]

DIVIDER_TOP = [[2]]
DIVIDER_BOTTOM = [[6]]

PACKETS.extend((DIVIDER_TOP, DIVIDER_BOTTOM))


def is_in_right_order(left: PairTyping, right: PairTyping) -> bool | None:
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return True
        if left > right:
            return False
        return None

    if isinstance(left, list) and isinstance(right, list):
        for l, r in zip_longest(left, right):
            if l is None:
                return True
            if r is None:
                return False

            result = is_in_right_order(l, r)

            if result is not None:
                return result

        return None

    if isinstance(left, list) and isinstance(right, int):
        return is_in_right_order(left, [right])

    if isinstance(left, int) and isinstance(right, list):
        return is_in_right_order([left], right)


def cmp_function(left: PairTyping, right: PairTyping) -> int:
    result = is_in_right_order(left, right)

    if result is True:
        return -1
    if result is False:
        return 1
    return 0


sorted_packets = sorted(PACKETS, key=cmp_to_key(cmp_function))

print(
    (sorted_packets.index(DIVIDER_TOP) + 1) * (sorted_packets.index(DIVIDER_BOTTOM) + 1)
)
