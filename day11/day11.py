import os.path
import sys
from math import floor

DATA = os.path.join(os.path.dirname(__file__), 'day11.txt')


def __north(pos) -> tuple:
    return pos[0] - 1, pos[1]


def __north_east(pos) -> tuple:
    if pos[1] % 2 == 0:
        return pos[0] - 1, pos[1] + 1
    return pos[0], pos[1] + 1


def __south_east(pos) -> tuple:
    if pos[1] % 2 == 0:
        return pos[0], pos[1] + 1
    return pos[0] + 1, pos[1] + 1


def __south(pos) -> tuple:
    return pos[0] + 1, pos[1]


def __south_west(pos) -> tuple:
    if pos[1] % 2 == 0:
        return pos[0], pos[1] - 1
    return pos[0] + 1, pos[1] - 1


def __north_west(pos) -> tuple:
    if pos[1] % 2 == 0:
        return pos[0] - 1, pos[1] - 1
    return pos[0], pos[1] - 1


# https://stackoverflow.com/a/35163351
def __distance(start, end) -> int:
    y1, y2, x1, x2 = start[0], end[0], start[1], end[1]

    du = x2 - x1
    dv = (y2 - floor(x2 / 2)) - (y1 - floor(x1 / 2))

    if (du >= 0 and dv >= 0) or (du < 0 and dv < 0):
        return abs(du) + abs(dv)
    return max(abs(du), abs(dv))


def __find_goal(data) -> (set, tuple):
    current_position = (0, 0)
    goal = (0, 0)
    positions = set()

    for direction in data.split(","):
        if direction == "n":
            current_position = __north(current_position)
        elif direction == "ne":
            current_position = __north_east(current_position)
        elif direction == "se":
            current_position = __south_east(current_position)
        elif direction == "s":
            current_position = __south(current_position)
        elif direction == "sw":
            current_position = __south_west(current_position)
        elif direction == "nw":
            current_position = __north_west(current_position)
        positions.add(current_position)
        goal = current_position

    return positions, goal


def calculate_steps(data) -> int:
    _, goal = __find_goal(data)
    return __distance((0, 0), goal)


def calculate_steps_furthest_from_start(data) -> int:
    positions, goal = __find_goal(data)
    positions.add((0, 0))
    max_steps, max_distance = -sys.maxsize - 1, -sys.maxsize - 1
    for p in positions:
        max_steps = max(max_steps, __distance((0, 0), p))
    return max_steps


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_steps(data)))
        print("Part 2: " + str(calculate_steps_furthest_from_start(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
