from itertools import zip_longest
import re

with open("day_05/input.txt") as file:
    CONFIGURATION, INSTRUCTIONS = file.read().split("\n\n")

instruction_regex = re.compile(r"move (?P<count>\d+) from (?P<from>\d+) to (?P<to>\d+)")

config_lines = CONFIGURATION.split("\n")
config_lines.pop()  # Remove the column count

column_count = (len(config_lines[-1]) + 1) // 4

rows = []
for raw_row in config_lines:
    row = []

    for i in range(column_count):
        if (4 * i + 1) > len(raw_row):
            break

        row.append(raw_row[4 * i + 1])
    rows.append(row)

columns = list(list(c) for c in zip_longest(*rows, fillvalue=" "))

for column in columns:
    column.reverse()

    while column[-1] == " ":
        column.pop()

for instruction in INSTRUCTIONS.split("\n"):
    match = instruction_regex.match(instruction)

    from_ = int(match.group("from")) - 1
    to = int(match.group("to")) - 1
    count = int(match.group("count"))

    columns[to].extend(columns[from_][-count:])
    columns[from_] = columns[from_][:-count]

print("".join(c[-1] for c in columns))
