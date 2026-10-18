import collections
import os.path
import sys

DATA = os.path.join(os.path.dirname(__file__), 'day08.txt')


_COMPARISONS = {
    ">": lambda left, right: left > right,
    "<": lambda left, right: left < right,
    ">=": lambda left, right: left >= right,
    "<=": lambda left, right: left <= right,
    "==": lambda left, right: left == right,
    "!=": lambda left, right: left != right,
}


def _evaluate_expressions(data) -> tuple[dict, int]:
    registers: dict = collections.defaultdict(lambda: 0)
    max_value = -sys.maxsize - 1
    for line in data.splitlines():
        register, operation, amount, _, condition_register, comparison, condition_value = (
            line.split(" "))

        if _COMPARISONS[comparison](registers[condition_register], int(condition_value)):
            if operation == "inc":
                registers[register] += int(amount)
            else:
                registers[register] -= int(amount)

        max_value = max(max_value, max(registers.values()))

    return registers, max_value


def find_largest_value_in_register(data) -> int:
    registers, _ = _evaluate_expressions(data)
    return max(registers.values())


def find_largest_value_during_process(data) -> int:
    _, max_value = _evaluate_expressions(data)
    return max_value


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_largest_value_in_register(data)))
        print("Part 2: " + str(find_largest_value_during_process(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
