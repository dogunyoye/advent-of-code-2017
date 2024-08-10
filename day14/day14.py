import os.path
from collections import Counter, deque

from day10.day10 import find_knot_hash

DATA = os.path.join(os.path.dirname(__file__), 'day14.txt')


def __build_grid(data) -> dict:
    depth = 0
    grid = {}

    for i in range(0, 128):
        key = data + "-" + str(i)
        knot_hash = find_knot_hash(key)
        knot_hash_binary = ""
        for j in range(0, len(knot_hash)):
            binary = format(int(knot_hash[j], 16), "b")
            pad = (4 - len(binary)) * "0"
            binary = pad + binary
            knot_hash_binary += binary

        for k in range(0, len(knot_hash_binary)):
            grid[(depth, k)] = knot_hash_binary[k]
        depth += 1

    return grid


def __bfs(start, grid, group_number, group) -> set:
    queue, visited = deque(), set()
    queue.append(start)
    visited.add(start)

    while len(queue) != 0:
        position = queue.popleft()
        group[position] = group_number
        i, j = position[0], position[1]

        neighbors = [(i, j - 1), (i - 1, j), (i, j + 1), (i + 1, j)]
        for n in neighbors:
            if n in grid and grid[n] == '1' and n not in visited:
                queue.append(n)
                visited.add(n)

    return visited


def calculate_number_of_used_squares(data) -> int:
    grid = __build_grid(data)
    return Counter(grid.values())['1']


def calculate_number_of_present_regions(data) -> int:
    grid = __build_grid(data)
    queue = deque()
    group = {}

    for i in range(0, 128):
        for j in range(0, 128):
            pos = (i, j)
            if grid[pos] == '1':
                queue.append(pos)

    grid_number = 1

    while len(queue) != 0:
        pos = queue.popleft()
        visited = __bfs(pos, grid, grid_number, group)
        for v in visited:
            if v in queue:
                queue.remove(v)
        grid_number += 1

    return len(set(group.values()))


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_number_of_used_squares(data)))
        print("Part 2: " + str(calculate_number_of_present_regions(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
