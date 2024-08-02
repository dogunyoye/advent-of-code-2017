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
        words = line.split(" ")
        valid = True
        for i in range(0, len(words)-1):
            first_bytes = sorted(words[i].encode('utf-8'))
            for j in range(i+1, len(words)):
                second_bytes = sorted(words[j].encode('utf-8'))
                if first_bytes == second_bytes:
                    valid = False
                    break

            if not valid:
                break

        if valid:
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
