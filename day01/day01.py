import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day01.txt')


def find_captcha_solution(data) -> int:
    result = 0
    for i in range(0, len(data)):
        if data[i] == data[(i + 1) % len(data)]:
            result += int(data[i])
    return result


def find_captcha_solution_part_two(data) -> int:
    result, jump = 0, int(len(data)/2)
    for i in range(0, len(data)):
        if data[i] == data[(i + jump) % len(data)]:
            result += int(data[i])
    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_captcha_solution(data)))
        print("Part 2: " + str(find_captcha_solution_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
