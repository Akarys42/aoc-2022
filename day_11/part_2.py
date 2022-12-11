import re
from collections import Counter
from functools import lru_cache
from math import lcm
from operator import add, mul

with open("day_11/input.txt") as file:
    MONKEY_DEFINITIONS = file.read().split("\n\n")


MONKEY_REGEX = re.compile(
    r"Monkey \d+:\n  Starting items: (?P<starting_items>[\d, ]+)\n"
    r"  Operation: new = (?P<operand_1>(\d+)|old) (?P<operator>\*|\+) (?P<operand_2>(\d+)|old)\n"
    r"  Test: divisible by (?P<test>\d+)\n"
    r"    If true: throw to monkey (?P<true_result>\d+)\n"
    r"    If false: throw to monkey (?P<false_result>\d+)"
)
ROUNDS = 10_000


class Monkey:
    def __init__(self, definition: str, monkey_list: list["Monkey"]) -> None:
        self.monkey_list = monkey_list
        self.total_thrown = 0

        match = MONKEY_REGEX.match(definition)

        self.items = Counter(
            int(i.strip()) for i in match.group("starting_items").split(",")
        )
        self.operand_1 = (
            "old"
            if match.group("operand_1") == "old"
            else int(match.group("operand_1"))
        )
        self.operand_2 = (
            "old"
            if match.group("operand_2") == "old"
            else int(match.group("operand_2"))
        )
        self.operator = match.group("operator")
        self.operator_function = add if match.group("operator") == "+" else mul
        self.test = int(match.group("test"))
        self.true_result_index = int(match.group("true_result"))
        self.false_result_index = int(match.group("false_result"))

    def round(self, least_common_multiple: int) -> None:
        for item, count in self.items.items():
            item, destination = self.destination_for(item, least_common_multiple)

            self.monkey_list[destination].throw(item, count)
            self.total_thrown += count

        self.items = {}

    @lru_cache(maxsize=1024)
    def destination_for(self, item: int, least_common_multiple: int) -> tuple[int, int]:
        operand_1 = item if self.operand_1 == "old" else self.operand_1
        operand_2 = item if self.operand_2 == "old" else self.operand_2

        item = self.operator_function(operand_1, operand_2) % least_common_multiple

        if item % self.test == 0:
            return item, self.true_result_index
        else:
            return item, self.false_result_index

    def throw(self, item: int, count: int) -> None:
        self.items[item] = self.items.get(item, 0) + count

    def __repr__(self) -> str:
        return f"<Monkey total_thrown={self.total_thrown}>"


monkey_list = []

for definition in MONKEY_DEFINITIONS:
    monkey_list.append(Monkey(definition, monkey_list))

least_common_multiple = lcm(*(monkey.test for monkey in monkey_list))

for _ in range(ROUNDS):
    for monkey in monkey_list:
        monkey.round(least_common_multiple)

monkey_list.sort(key=lambda m: m.total_thrown, reverse=True)
print(monkey_list[0].total_thrown * monkey_list[1].total_thrown)
