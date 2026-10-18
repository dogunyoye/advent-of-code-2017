import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day04.txt')


def find_valid_passphrases(data) -> int:
    result = 0
    for line in data.splitlines():
        words = set()
        valid = True
        for word in line.split(" "):
            if word in words:
                valid = False
                break
            words.add(word)

        if valid:
            result += 1

    return result


def find_valid_passphrases_with_extra_security(data) -> int:
    result = 0
    for line in data.splitlines():
        signatures = ["".join(sorted(word)) for word in line.split(" ")]
        if len(signatures) == len(set(signatures)):
            result += 1

    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_valid_passphrases(data)))
        print("Part 2: " + str(find_valid_passphrases_with_extra_security(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
