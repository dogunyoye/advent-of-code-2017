import os.path
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day16.txt')


def __spin(programs, start_idx) -> list:
    rot = deque(programs)
    rot.rotate(start_idx)
    return list(rot)


def __exchange(programs, first_idx, second_idx) -> list:
    first = programs[first_idx]
    temp = first
    programs[first_idx] = programs[second_idx]
    programs[second_idx] = temp
    return programs


def __partner(programs, first_elem, second_elem) -> list:
    first_idx = programs.index(first_elem)
    second_idx = programs.index(second_elem)
    return __exchange(programs, first_idx, second_idx)


def __dance(programs, data) -> str:
    for parts in data.split(","):
        instruction = parts[0]
        if instruction == 's':
            start_idx = int(parts[1:])
            programs = __spin(programs, start_idx)
        elif instruction == 'x':
            fs = parts[1:].split("/")
            programs = __exchange(programs, int(fs[0]), int(fs[1]))
        elif instruction == 'p':
            fs = parts[1:].split("/")
            programs = __partner(programs, fs[0], fs[1])
    return "".join(programs)


def find_program_order(data) -> str:
    programs = []
    for i in range(ord('a'), ord('q')):
        programs.append(chr(i))

    return __dance(programs, data)


def find_program_order_after_a_billion_dances(data) -> str:
    runs = 1_000_000_000
    one_dance = find_program_order(data)
    current_dance = one_dance
    dances = [one_dance]
    cycle = 0

    while runs != 0:
        runs -= 1
        current_dance = __dance(list(current_dance), data)
        if current_dance == one_dance:
            cycle = 1_000_000_000 - runs
            break
        dances.append(current_dance)

    return dances[(1_000_000_000 % cycle) - 1]


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_program_order(data))
        print("Part 2: " + find_program_order_after_a_billion_dances(data))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
