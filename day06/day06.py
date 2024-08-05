import os.path
import sys

DATA = os.path.join(os.path.dirname(__file__), 'day06.txt')


def __find_cycle(data, seen_count) -> int:
    blocks = [eval(i) for i in data.split("\t")]
    seen, cycle_count = set(), 0
    prev_cycles, cycles = 0, 0
    seen_config = tuple()

    while True:
        largest_num, largest_idx = -sys.maxsize - 1, -sys.maxsize - 1
        for idx, i in enumerate(blocks):
            if i > largest_num:
                largest_num = i
                largest_idx = idx

        blocks[largest_idx] = 0

        for i in range(0, largest_num):
            blocks[(largest_idx + i + 1) % len(blocks)] += 1

        cycles += 1

        config = tuple(blocks)
        if config in seen:
            if seen_count == 1:
                return cycles

            if cycle_count == 0:
                prev_cycles = cycles
                seen_config = config

            cycle_count += 1

            if seen_count <= cycle_count and config == seen_config:
                return cycles - prev_cycles

        seen.add(config)


def find_number_of_cycles_before_duplicate(data) -> int:
    return __find_cycle(data, 1)


def find_cycle_length(data) -> int:
    return __find_cycle(data, 2)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_cycles_before_duplicate(data)))
        print("Part 2: " + str(find_cycle_length(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
