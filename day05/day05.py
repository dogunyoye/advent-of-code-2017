import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day05.txt')


def find_number_of_steps_to_reach_exit(data) -> int:
    result, current_idx = 0, 0
    instructions = [eval(i) for i in data.splitlines()]

    while current_idx < len(instructions):
        offset = instructions[current_idx]
        instructions[current_idx] += 1
        current_idx += offset
        result += 1

    return result


def find_number_of_steps_to_reach_exit_part_two(data) -> int:
    result, current_idx = 0, 0
    instructions = [eval(i) for i in data.splitlines()]

    while current_idx < len(instructions):
        offset = instructions[current_idx]
        if offset >= 3:
            instructions[current_idx] -= 1
        else:
            instructions[current_idx] += 1

        current_idx += offset
        result += 1

    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_steps_to_reach_exit(data)))
        print("Part 2: " + str(find_number_of_steps_to_reach_exit_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
