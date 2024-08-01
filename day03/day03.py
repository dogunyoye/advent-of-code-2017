import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day03.txt')


def __manhattan_distance(start, end) -> int:
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def __sum_neighbours(current_position, grid) -> int:
    result = 0
    neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]
    for n in neighbours:
        pos = (current_position[0] + n[0], current_position[1] + n[1])
        if pos in grid:
            result += grid[pos]

    return result


def find_manhattan_distance_to_access_point(data) -> int:
    current_position = (0, 0)
    current_number = 1
    goal = int(data)
    steps = 1

    while True:
        # move east
        for i in range(0, steps):
            current_position = (current_position[0], current_position[1] + 1)
            current_number += 1
            if current_number == goal:
                return __manhattan_distance((0, 0), current_position)

        # move north
        for i in range(0, steps):
            current_position = (current_position[0] - 1, current_position[1])
            current_number += 1
            if current_number == goal:
                return __manhattan_distance((0, 0), current_position)

        steps += 1

        # move west
        for i in range(0, steps):
            current_position = (current_position[0], current_position[1] - 1)
            current_number += 1
            if current_number == goal:
                return __manhattan_distance((0, 0), current_position)

        # move south
        for i in range(0, steps):
            current_position = (current_position[0] + 1, current_position[1])
            current_number += 1
            if current_number == goal:
                return __manhattan_distance((0, 0), current_position)

        steps += 1


def find_manhattan_distance_to_access_point_part_two(data) -> int:
    grid = {(0, 0): 1}
    current_position = (0, 0)
    goal = int(data)
    steps = 1

    while True:
        # move east
        for _ in range(0, steps):
            current_position = (current_position[0], current_position[1] + 1)
            current_number = __sum_neighbours(current_position, grid)
            if current_number > goal:
                return current_number
            grid[current_position] = current_number

        # move north
        for _ in range(0, steps):
            current_position = (current_position[0] - 1, current_position[1])
            current_number = __sum_neighbours(current_position, grid)
            if current_number > goal:
                return current_number
            grid[current_position] = current_number

        steps += 1

        # move west
        for _ in range(0, steps):
            current_position = (current_position[0], current_position[1] - 1)
            current_number = __sum_neighbours(current_position, grid)
            if current_number > goal:
                return current_number
            grid[current_position] = current_number

        # move south
        for _ in range(0, steps):
            current_position = (current_position[0] + 1, current_position[1])
            current_number = __sum_neighbours(current_position, grid)
            if current_number > goal:
                return current_number
            grid[current_position] = current_number

        steps += 1


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_manhattan_distance_to_access_point(data)))
        print("Part 2: " + str(find_manhattan_distance_to_access_point_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
