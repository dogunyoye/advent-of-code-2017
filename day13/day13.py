import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day13.txt')


def _build_firewall(data) -> tuple[dict, tuple]:
    firewall = {}
    for line in data.splitlines():
        parts = line.split(": ")
        layer, range_size = int(parts[0]), int(parts[1])

        indices = list(range(range_size))
        indices.extend(range(max(indices) - 1, 0, -1))

        firewall[layer] = (range_size, (layer, 0), indices)
    return firewall, (max(firewall.keys()), 0)


def calculate_severity(data) -> int:
    firewall, goal = _build_firewall(data)
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


# optimised solution based on:
# https://gist.github.com/snarkbait/e6812b39ce04af2c18db9dfd95e1ea10
def calculate_smallest_delay_remain_undetected(data) -> int:
    firewall, _ = _build_firewall(data)
    delay = 2

    while True:
        caught = False
        for k, v in firewall.items():
            if ((k + delay) % ((v[0] - 1) * 2)) == 0:
                caught = True
                break

        if not caught:
            break
        delay += 2

    return delay


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_severity(data)))
        print("Part 2: " + str(calculate_smallest_delay_remain_undetected(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
