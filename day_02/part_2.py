with open("day_02/input.txt") as file:
    INPUT = file.readlines()


HUMAN_NAMES = {"A": "rock", "B": "paper", "C": "scissors"}

WIN_CASES = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
LOOSE_CASES = {b: a for a, b in WIN_CASES.items()}
DRAW_CASES = {a: a for a in HUMAN_NAMES.values()}

CASES = {"X": (LOOSE_CASES, 0), "Y": (DRAW_CASES, 3), "Z": (WIN_CASES, 6)}

POINTS = {"rock": 1, "paper": 2, "scissors": 3}


def calculate_score(opponent: str, strategy: str) -> int:
    cases, outcome_points = CASES[strategy]

    play_points = POINTS[cases[HUMAN_NAMES[opponent]]]

    return outcome_points + play_points


print(sum(calculate_score(case[0], case[2]) for case in INPUT))
