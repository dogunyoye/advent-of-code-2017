import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day15.txt')

GENERATOR_A_FACTOR = 16807
GENERATOR_B_FACTOR = 48271
MODULUS = 2147483647
LOW_16_BITS_MASK = 0xFFFF

TOTAL_PAIRS = 40_000_000
PART_TWO_MULTIPLE_A = 4
PART_TWO_MULTIPLE_B = 8


def _seeds(data) -> tuple[int, int]:
    lines = data.splitlines()
    return int(lines[0].split(" ")[-1]), int(lines[1].split(" ")[-1])


def _generator(seed, factor, multiple=1):
    value = seed
    while True:
        value = (value * factor) % MODULUS
        if value % multiple == 0:
            yield value


def _count_matching_pairs(data, pairs, multiple_a=1, multiple_b=1) -> int:
    seed_a, seed_b = _seeds(data)
    generator_a = _generator(seed_a, GENERATOR_A_FACTOR, multiple_a)
    generator_b = _generator(seed_b, GENERATOR_B_FACTOR, multiple_b)

    count = 0
    for _ in range(pairs):
        match = (next(generator_a) & LOW_16_BITS_MASK) == (
            next(generator_b) & LOW_16_BITS_MASK
        )
        if match:
            count += 1

    return count


def calculate_final_count(data) -> int:
    return _count_matching_pairs(data, TOTAL_PAIRS)


def calculate_final_count_part_two(data) -> int:
    return _count_matching_pairs(
        data, 5_000_000, PART_TWO_MULTIPLE_A, PART_TWO_MULTIPLE_B
    )


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_final_count(data)))
        print("Part 2: " + str(calculate_final_count_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
