with open("day_10/input.txt") as file:
    INSTRUCTIONS = [line.strip() for line in file.readlines()]


class Emulator:
    def __init__(self, instructions: list[str]) -> None:
        self.instructions = instructions
        self.cycle = 0
        self.output = 0
        self.x = 1

    def increase_cycle_count(self) -> None:
        self.cycle += 1

        scan_index = (self.cycle - 1) % 40

        if abs(scan_index - self.x) < 2:
            print("█", end="")
        else:
            print(" ", end="")

        if (self.cycle % 40) == 0:
            print("")

    def noop(self) -> None:
        self.increase_cycle_count()

    def addx(self, operand: int) -> None:
        self.increase_cycle_count()
        self.increase_cycle_count()
        self.x += operand

    def run(self) -> int:
        for instruction in self.instructions:
            if instruction == "noop":
                self.noop()
            elif instruction.startswith("addx"):
                self.addx(int(instruction.removeprefix("addx ")))
            else:
                raise ValueError(f"Unknown instruction {instruction!r}")

        return self.output


Emulator(INSTRUCTIONS).run()
