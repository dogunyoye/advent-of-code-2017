import os.path
from math import floor

DATA = os.path.join(os.path.dirname(__file__), 'day11.txt')


def _north(pos) -> tuple:
    return pos[0] - 1, pos[1]


def _north_east(pos) -> tuple:
    if pos[1] % 2 == 0:
        return pos[0] - 1, pos[1] + 1
    return pos[0], pos[1] + 1


def _south_east(pos) -> tuple:
    if pos[1] % 2 == 0:
        return pos[0], pos[1] + 1
    return pos[0] + 1, pos[1] + 1


def _south(pos) -> tuple:
    return pos[0] + 1, pos[1]


def _south_west(pos) -> tuple:
    if pos[1] % 2 == 0:
        return pos[0], pos[1] - 1
    return pos[0] + 1, pos[1] - 1


def _north_west(pos) -> tuple:
    if pos[1] % 2 == 0:
        return pos[0] - 1, pos[1] - 1
    return pos[0], pos[1] - 1


# https://stackoverflow.com/a/35163351
def _distance(start, end) -> int:
    y1, y2, x1, x2 = start[0], end[0], start[1], end[1]

    du = x2 - x1
    dv = (y2 - floor(x2 / 2)) - (y1 - floor(x1 / 2))

    if (du >= 0 and dv >= 0) or (du < 0 and dv < 0):
        return abs(du) + abs(dv)
    return max(abs(du), abs(dv))


def _find_goal(data) -> tuple[tuple, int]:
    current_position = (0, 0)
    goal = (0, 0)
    max_distance = 0

    for direction in data.split(","):
        if direction == "n":
            current_position = _north(current_position)
        elif direction == "ne":
            current_position = _north_east(current_position)
        elif direction == "se":
            current_position = _south_east(current_position)
        elif direction == "s":
            current_position = _south(current_position)
        elif direction == "sw":
            current_position = _south_west(current_position)
        elif direction == "nw":
            current_position = _north_west(current_position)
        goal = current_position
        max_distance = max(max_distance, _distance((0, 0), current_position))

    return goal, max_distance


def calculate_steps(data) -> int:
    goal, _ = _find_goal(data)
    return _distance((0, 0), goal)


def calculate_steps_furthest_from_start(data) -> int:
    _, max_distance = _find_goal(data)
    return max_distance


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_steps(data)))
        print("Part 2: " + str(calculate_steps_furthest_from_start(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
