with open("day_10/input.txt") as file:
    INSTRUCTIONS = [line.strip() for line in file.readlines()]


SIGNAl_CYCLES = [20, 60, 100, 140, 180, 220]


class Emulator:
    def __init__(self, instructions: list[str], signal_cycles: list[int]) -> None:
        self.instructions = instructions
        self.signal_cycles = signal_cycles
        self.cycle = 0
        self.output = 0
        self.x = 1

    def increase_cycle_count(self) -> None:
        self.cycle += 1
        if self.cycle in self.signal_cycles:
            self.output += self.x * self.cycle

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


print(Emulator(INSTRUCTIONS, SIGNAl_CYCLES).run())
