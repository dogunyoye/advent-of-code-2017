import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day09.txt')


def __collect_groups(data) -> dict:
    groups = {}
    for line_idx, line in enumerate(data.splitlines()):
        stack = []
        canceled = False
        garbage = False
        for i in range(0, len(line)):

            if canceled:
                canceled = False
                continue

            if line[i] == '!':
                canceled = True
                continue

            if line[i] == '<':
                garbage = True
            elif line[i] == '>':
                garbage = False

            if line[i] == '{' and not garbage:
                stack.append(i)
            elif line[i] == '}' and not garbage:
                score = len(stack)
                start_idx = stack.pop()
                groups[(line_idx, start_idx, i)] = score

    return groups


def __is_valid_group(segment) -> bool:
    garbage_opened, garbage_closed = False, False
    skip = False

    for i in range(0, len(segment)):
        if skip:
            skip = False
            continue

        if segment[i] == '!':
            skip = True
            continue

        if segment[i] == '<':
            garbage_opened = True
        elif segment[i] == '>':
            garbage_closed = True

    if not garbage_opened and not garbage_closed:
        return True

    if garbage_opened and garbage_closed:
        return True

    return False


def calculate_total_score(data) -> int:
    score = 0
    lines = data.splitlines()
    for k, v in __collect_groups(data).items():
        segment = lines[k[0]][k[1]:k[2] + 1]
        if __is_valid_group(segment):
            score += v

    return score


def find_non_canceled_characters_within_garbage(data) -> int:
    counting, skip = False, False
    count, result = 0, 0

    for i in range(0, len(data)):
        if skip:
            skip = False
            continue

        if data[i] == '<':
            if counting:
                count += 1
                continue
            counting = True
            continue
        elif data[i] == '>':
            counting = False
            result += count
            count = 0
            continue

        if data[i] == '!':
            skip = True
            continue

        if counting:
            count += 1

    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_total_score(data)))
        print("Part 2: " + str(find_non_canceled_characters_within_garbage(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
