import os.path
from enum import Enum

DATA = os.path.join(os.path.dirname(__file__), 'day22.txt')


class Direction(Enum):
    NORTH = 1
    EAST = 2
    SOUTH = 3
    WEST = 4


def __build_grid(lines) -> dict:
    grid = {}
    for i, line in enumerate(lines):
        for j in range(0, len(line)):
            grid[(i, j)] = line[j]
    return grid


# Directions in clockwise order, so a turn is a rotation around this tuple.
DIRECTIONS = (Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST)
MOVEMENTS = {
    Direction.NORTH: (-1, 0),
    Direction.EAST: (0, 1),
    Direction.SOUTH: (1, 0),
    Direction.WEST: (0, -1),
}


def __turn_left(facing) -> Direction:
    index = DIRECTIONS.index(facing)
    return DIRECTIONS[(index - 1) % len(DIRECTIONS)]


def __turn_right(facing) -> Direction:
    index = DIRECTIONS.index(facing)
    return DIRECTIONS[(index + 1) % len(DIRECTIONS)]


def __reverse(facing) -> Direction:
    index = DIRECTIONS.index(facing)
    return DIRECTIONS[(index + 2) % len(DIRECTIONS)]


def __move(current_position, facing) -> tuple[int, int]:
    row, column = MOVEMENTS[facing]
    return current_position[0] + row, current_position[1] + column


def find_number_of_bursts_that_infect_a_node(data) -> int:
    lines = data.splitlines()
    grid = __build_grid(lines)
    current_position, current_direction = (len(lines) // 2, len(lines[0]) // 2), Direction.NORTH
    bursts, infection_bursts = 10000, 0

    while bursts != 0:
        node_status = '.'
        if current_position in grid and grid[current_position] == '#':
            node_status = '#'
            current_direction = __turn_right(current_direction)
        else:
            current_direction = __turn_left(current_direction)

        if node_status == '.':
            node_status = '#'
            infection_bursts += 1
        else:
            node_status = '.'

        grid[current_position] = node_status
        current_position = __move(current_position, current_direction)
        bursts -= 1
    return infection_bursts


def find_number_of_bursts_that_infect_a_node_with_new_rules(data) -> int:
    lines = data.splitlines()
    grid = __build_grid(lines)
    current_position, current_direction = (len(lines) // 2, len(lines[0]) // 2), Direction.NORTH
    bursts, infection_bursts = 10000000, 0

    while bursts != 0:
        node_status = '.'
        if current_position in grid:
            node_status = grid[current_position]

        if node_status == '.':
            node_status = 'W'
            current_direction = __turn_left(current_direction)
        elif node_status == 'W':
            node_status = '#'
            infection_bursts += 1
        elif node_status == '#':
            node_status = 'F'
            current_direction = __turn_right(current_direction)
        elif node_status == 'F':
            node_status = '.'
            current_direction = __reverse(current_direction)

        grid[current_position] = node_status
        current_position = __move(current_position, current_direction)
        bursts -= 1
    return infection_bursts


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_bursts_that_infect_a_node(data)))
        print("Part 2: " + str(find_number_of_bursts_that_infect_a_node_with_new_rules(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
