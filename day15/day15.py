import os.path
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day15.txt')


def calculate_final_count(data) -> int:
    lines = data.splitlines()
    gen_a = int(lines[0].split(" ")[4])
    gen_b = int(lines[1].split(" ")[4])
    runs = 40_000_000
    count = 0

    while runs != 0:
        gen_a = (gen_a * 16807) % 2147483647
        gen_b = (gen_b * 48271) % 2147483647

        gen_a_binary = format(gen_a, 'b')
        gen_b_binary = format(gen_b, 'b')

        if gen_a_binary[len(gen_a_binary) - 16:] == gen_b_binary[len(gen_b_binary) - 16:]:
            count += 1

        runs -= 1
    return count


def calculate_final_count_part_two(data) -> int:
    lines = data.splitlines()
    gen_a = int(lines[0].split(" ")[4])
    gen_b = int(lines[1].split(" ")[4])
    gen_a_queue, gen_b_queue = deque(), deque()
    runs = 5_000_000
    count = 0

    while runs != 0:
        gen_a = (gen_a * 16807) % 2147483647
        gen_b = (gen_b * 48271) % 2147483647

        if gen_a % 4 == 0:
            gen_a_queue.append(format(gen_a, 'b'))
        if gen_b % 8 == 0:
            gen_b_queue.append(format(gen_b, 'b'))

        if len(gen_a_queue) > 0 and len(gen_b_queue) > 0:
            gen_a_binary = gen_a_queue.popleft()
            gen_b_binary = gen_b_queue.popleft()
            if gen_a_binary[len(gen_a_binary) - 16:] == gen_b_binary[len(gen_b_binary) - 16:]:
                count += 1
            runs -= 1

    return count


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_final_count(data)))
        print("Part 2: " + str(calculate_final_count_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
