import os.path
import sys

DATA = os.path.join(os.path.dirname(__file__), 'day02.txt')


def calculate_spreadsheet_checksum(data) -> int:
    result = 0
    for line in data.splitlines():
        nums = line.split("\t")
        min_num, max_num = sys.maxsize, -sys.maxsize - 1
        for n in nums:
            min_num = min(min_num, int(n))
            max_num = max(max_num, int(n))
        result += max_num - min_num
    return result


def calculate_spreadsheet_checksum_part_two(data) -> int:
    result = 0
    for line in data.splitlines():
        nums = line.split("\t")
        for i in range(0, len(nums)):
            found = False
            first = int(nums[i])
            for j in range(i+1, len(nums)):
                second = int(nums[j])
                if first % second == 0:
                    result += int(first / second)
                    found = True
                    break

                if second % first == 0:
                    result += int(second / first)
                    found = True
                    break
            if found:
                break
    return result


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_spreadsheet_checksum(data)))
        print("Part 2: " + str(calculate_spreadsheet_checksum_part_two(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
