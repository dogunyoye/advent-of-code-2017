from collections import defaultdict, Counter


# HARDCODED BLUEPRINT INSTRUCTIONS
def find_diagnostic_checksum() -> int:
    steps = 12317297
    state = 'A'
    current_position = 0
    tape = defaultdict(lambda: 0)

    while steps != 0:
        if state == 'A':
            if tape[current_position] == 0:
                tape[current_position] = 1
                current_position += 1
                state = 'B'
            else:
                tape[current_position] = 0
                current_position -= 1
                state = 'D'
        elif state == 'B':
            if tape[current_position] == 0:
                tape[current_position] = 1
                current_position += 1
                state = 'C'
            else:
                tape[current_position] = 0
                current_position += 1
                state = 'F'
        elif state == 'C':
            if tape[current_position] == 0:
                state = 'C'
            else:
                state = 'A'
            tape[current_position] = 1
            current_position -= 1
        elif state == 'D':
            if tape[current_position] == 0:
                tape[current_position] = 0
                current_position -= 1
                state = 'E'
            else:
                tape[current_position] = 1
                current_position += 1
                state = 'A'
        elif state == 'E':
            if tape[current_position] == 0:
                tape[current_position] = 1
                current_position -= 1
                state = 'A'
            else:
                tape[current_position] = 0
                current_position += 1
                state = 'B'
        elif state == 'F':
            if tape[current_position] == 0:
                state = 'C'
            else:
                state = 'E'
            tape[current_position] = 0
            current_position += 1
        steps -= 1

    return Counter(tape.values())[1]


def main() -> int:
    print("Part 1: " + str(find_diagnostic_checksum()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
