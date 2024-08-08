import os.path
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day12.txt')


def __build_map(data) -> dict:
    grid = {}
    for line in data.splitlines():
        parts = line.split(" <-> ")
        parent = int(parts[0])
        children = []
        for c in parts[1].split(", "):
            children.append(int(c))
        grid[parent] = children
    return grid


def __dfs(grid, parent, visited) -> int:
    if parent in visited:
        return 0

    visited.add(parent)
    result = 1
    for c in grid[parent]:
        result += __dfs(grid, c, visited)
    return result


def find_number_of_programs_connected_to_zero(data) -> int:
    grid = __build_map(data)
    return __dfs(grid, 0, set())


def find_number_of_groups(data) -> int:
    grid = __build_map(data)
    queue = deque()
    queue.extend(grid.keys())
    groups = 0

    while len(queue) != 0:
        current = queue.popleft()
        visited = set()
        __dfs(grid, current, visited)

        for c in visited:
            if c in queue:
                queue.remove(c)
        groups += 1

    return groups


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_programs_connected_to_zero(data)))
        print("Part 2: " + str(find_number_of_groups(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
