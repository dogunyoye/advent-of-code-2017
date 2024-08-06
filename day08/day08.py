import collections
import os.path
import sys

DATA = os.path.join(os.path.dirname(__file__), 'day08.txt')


def __evaluate_expressions(data) -> (dict, int):
    registers = collections.defaultdict(lambda: 0)
    max_value = -sys.maxsize - 1
    for line in data.splitlines():
        parts = line.split(" ")

        if parts[1] == "dec":
            parts[1] = "-"
        else:
            parts[1] = "+"

        conditional = " ".join([parts[4], parts[5], parts[6]])
        action = " ".join([parts[0], parts[1], parts[2]])

        if eval(conditional, {}, registers):
            registers[parts[0]] = eval(action, {}, registers)
        max_value = max(max_value, max(registers.values()))

    return registers, max_value


def find_largest_value_in_register(data) -> int:
    registers, _ = __evaluate_expressions(data)
    return max(registers.values())


def find_largest_value_during_process(data) -> int:
    _, max_value = __evaluate_expressions(data)
    return max_value


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_largest_value_in_register(data)))
        print("Part 2: " + str(find_largest_value_during_process(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
