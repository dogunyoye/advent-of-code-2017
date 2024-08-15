import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day19.txt')


def __build_route(data) -> dict:
    route = {}
    depth = 0
    track = {'|', '-', '+'}
    for line in data.splitlines():
        for j in range(0, len(line)):
            if line[j].isalpha() or line[j] in track:
                route[(depth, j)] = line[j]
        depth += 1
    return route


def find_route(data) -> (str, int):
    route = __build_route(data)
    current_pos = list(filter(lambda coord: coord[0] == 0, route.keys()))[0]
    direction = 0
    neighbors = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    visited = set()
    visited.add(current_pos)
    path = ""
    steps = 0

    for i, n in enumerate(neighbors):
        next_pos = (current_pos[0] + n[0], current_pos[1] + n[1])
        if next_pos in route:
            direction = i
            break

    while current_pos in route:
        while current_pos in route and route[current_pos] != '+':
            steps += 1
            if route[current_pos].isalpha():
                path += str(route[current_pos])
            current_pos = (current_pos[0] + neighbors[direction][0], current_pos[1] + neighbors[direction][1])
            visited.add(current_pos)

        for i, n in enumerate(neighbors):
            next_pos = (current_pos[0] + n[0], current_pos[1] + n[1])
            if next_pos in route and next_pos not in visited:
                direction = i
                break

        current_pos = (current_pos[0] + neighbors[direction][0], current_pos[1] + neighbors[direction][1])
        visited.add(current_pos)
        steps += 1

    return path, steps - 1


def calculate_number_of_steps(data) -> int:
    return find_route(data)[1]


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_route(data)[0])
        print("Part 2: " + str(calculate_number_of_steps(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
