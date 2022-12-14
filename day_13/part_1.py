from itertools import zip_longest
import ast

with open("day_13/input.txt") as file:
    PAIRS = [
        [ast.literal_eval(line) for line in chunk.split("\n")]
        for chunk in file.read().split("\n\n")
    ]

PairTyping = int | list["PairTyping"]


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


print(sum(i + 1 for i, pair in enumerate(PAIRS) if is_in_right_order(*pair)))
