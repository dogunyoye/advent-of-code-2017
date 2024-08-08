import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day10.txt')


def calculate_product_of_first_two_numbers(data) -> int:
    lengths = [eval(i) for i in data.split(",")]
    skip, idx = 0, 0
    nums = []
    for i in range(0, 256):
        nums.append(i)

    for length in lengths:
        sublist = []
        for i in range(idx, idx + length):
            sublist.append(nums[i % len(nums)])
        sublist.reverse()

        for count, i in enumerate(range(idx, idx + length)):
            nums[i % len(nums)] = sublist[count]

        idx += length + skip
        skip += 1

    return nums[0] * nums[1]


def find_knot_hash(data) -> str:
    ascii_data = []
    extra_data = [17, 31, 73, 47, 23]
    rounds = 64

    for i in range(0, len(data)):
        ascii_data.append(ord(data[i]))
    ascii_data.extend(extra_data)

    skip, idx = 0, 0
    nums = []
    for i in range(0, 256):
        nums.append(i)

    while rounds != 0:
        for length in ascii_data:
            sublist = []
            for i in range(idx, idx + length):
                sublist.append(nums[i % len(nums)])
            sublist.reverse()

            for count, i in enumerate(range(idx, idx + length)):
                nums[i % len(nums)] = sublist[count]

            idx += length + skip
            skip += 1
        rounds -= 1

    dense_hash = []
    knot_hash = ""

    for i in range(0, len(nums), 16):
        block = nums[i:i+16]
        value = block[0] ^ block[1]
        for j in range(2, len(block)):
            value ^= block[j]
        dense_hash.append(value)

    for i in range(0, len(dense_hash)):
        s = format(dense_hash[i], 'x')
        if len(s) == 1:
            s = '0' + s
        knot_hash += s

    return knot_hash


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(calculate_product_of_first_two_numbers(data)))
        print("Part 2: " + str(find_knot_hash(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
