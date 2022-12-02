with open("day_02/input.txt") as file:
    INPUT = file.readlines()

WINS = [("A", "Y"), ("B", "Z"), ("C", "X")]
DRAWS = [("A", "X"), ("B", "Y"), ("C", "Z")]
POINTS = {"X": 1, "Y": 2, "Z": 3}


def calculate_score(opponent: str, myself: str) -> int:
    extra = 0
    if (opponent, myself) in DRAWS:
        extra = 3
    if (opponent, myself) in WINS:
        extra = 6

    return POINTS[myself] + extra


print(sum(calculate_score(case[0], case[2]) for case in INPUT))
