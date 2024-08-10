import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day13.txt')


def __build_firewall(data) -> (dict, tuple):
    firewall = {}
    for line in data.splitlines():
        parts = line.split(": ")
        layer, range_size = int(parts[0]), int(parts[1])

        indices = []
        for i in range(0, range_size):
            indices.append(i)
        for i in range(max(indices) - 1, 0, -1):
            indices.append(i)

        firewall[layer] = (range_size, (layer, 0), indices)
    return firewall, (max(firewall.keys()), 0)


def __copy_firewall(firewall) -> dict:
    copy = {}
    for k, v in firewall.items():
        copy[k] = (v[0], (v[1][0], v[1][1]), v[2].copy())
    return copy


def calculate_severity(data) -> int:
    firewall, goal = __build_firewall(data)
    current_position = (-1, 0)
    caught = []
    picoseconds = 0

    while True:
        current_position = (current_position[0] + 1, current_position[1])

        for k, v in firewall.items():
            if v[1] == current_position:
                caught.append((k, v[0]))

        for k, v in firewall.items():
            pos, indices = v[1], v[2]
            firewall[k] = (v[0], (pos[0], indices[(picoseconds + 1) % len(indices)]), indices)

        picoseconds += 1

        if current_position == goal:
            break

    severity = 0
    for c in caught:
        severity += c[0] * c[1]

    return severity


# works but takes a non-optimal time to return
def calculate_smallest_delay_remain_undetected(data) -> int:
    delay = 0
    firewall, goal = __build_firewall(data)

    while True:
        delay += 1

        for k, v in firewall.items():
            pos, indices = v[1], v[2]
            firewall[k] = (v[0], (pos[0], indices[delay % len(indices)]), indices)

        firewall_copy = __copy_firewall(firewall)
        current_position = (-1, 0)
        picoseconds = delay

        while True:
            current_position = (current_position[0] + 1, current_position[1])
            caught = False

            for k, v in firewall_copy.items():
                if v[1] == current_position:
                    caught = True
                    break

            if caught:
                break

            for k, v in firewall_copy.items():
                pos, indices = v[1], v[2]
                firewall_copy[k] = (v[0], (pos[0], indices[(picoseconds + 1) % len(indices)]), indices)

            picoseconds += 1

            if current_position == goal:
                return delay


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_severity(data)))
        print("Part 2: " + str(calculate_smallest_delay_remain_undetected(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
