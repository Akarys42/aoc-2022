from dataclasses import dataclass, field
from typing import Optional, Union


@dataclass
class Directory:
    previous_dir: Optional["Directory"]
    content: dict[str, Union["Directory", "File"]] = field(default_factory=dict)
    total_size: Optional[int] = None


@dataclass
class File:
    size: int


with open("day_07/input.txt") as file:
    INSTRUCTIONS = file.read().split("$")

ROOT = Directory(None)
active_directory = ROOT
all_dirs = [ROOT]


for instruction in INSTRUCTIONS:
    instruction = instruction.strip()

    if instruction == "cd /":
        active_directory = ROOT

    elif instruction == "cd ..":
        active_directory = active_directory.previous_dir

    elif instruction.startswith("cd"):
        folder_name = instruction.removeprefix("cd").strip()

        if folder_name not in active_directory.content:
            active_directory.content[folder_name] = Directory(active_directory)
            all_dirs.append(active_directory.content[folder_name])

        active_directory = active_directory.content[folder_name]

    elif instruction.startswith("ls"):
        lines = instruction.splitlines()[1:]

        for line in lines:
            meta, name = line.split(" ")

            if meta == "dir":
                active_directory.content[name] = Directory(active_directory)
                all_dirs.append(active_directory.content[name])
            else:
                active_directory.content[name] = File(int(meta))


def compute_total_size(dir: Directory) -> int:
    if dir.total_size:
        return dir.total_size

    total = 0

    for content in dir.content.values():
        if isinstance(content, File):
            total += content.size
        elif isinstance(content, Directory):
            if not content.total_size:
                content.total_size = compute_total_size(content)
            total += content.total_size
        else:
            raise ValueError(f"What is this doing here? {content}")

    return total


free_space = 70_000_000 - compute_total_size(ROOT)
needed_space = 30_000_000 - free_space

large_enough_dirs = [dir for dir in all_dirs if compute_total_size(dir) >= needed_space]
large_enough_dirs.sort(key=lambda d: compute_total_size(d))

print(compute_total_size(large_enough_dirs[0]))
