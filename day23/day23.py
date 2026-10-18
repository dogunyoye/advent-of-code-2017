import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day23.txt')


def _is_prime(value) -> bool:
    if value < 2:
        return False
    if value % 2 == 0:
        return value == 2

    divisor = 3
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 2

    return True


def _set(registers, register, value):
    if value.isalpha():
        registers[register] = registers[value]
        return
    registers[register] = int(value)


def _sub(registers, register, value):
    if value.isalpha():
        registers[register] -= registers[value]
        return
    registers[register] -= int(value)


def _mul(registers, register, value):
    if value.isalpha():
        registers[register] *= registers[value]
        return
    registers[register] *= int(value)


def _jnz(instruction_pointer, registers, value0, value1) -> int:
    v0 = registers[value0] if value0.isalpha() else int(value0)
    v1 = registers[value1] if value1.isalpha() else int(value1)

    if v0 != 0:
        return instruction_pointer + v1
    return instruction_pointer + 1


def _initialise_registers() -> dict:
    registers = {}
    for r in range(ord('a'), ord('i')):
        registers[chr(r)] = 0
    return registers


def find_number_of_times_mul_is_invoked(data) -> int:
    registers = _initialise_registers()
    instructions = data.splitlines()
    instruction_pointer, mul_count = 0, 0

    while instruction_pointer < len(instructions):
        parts = instructions[instruction_pointer].split(" ")
        instruction = parts[0]
        if instruction == "set":
            _set(registers, parts[1], parts[2])
        elif instruction == "sub":
            _sub(registers, parts[1], parts[2])
        elif instruction == "mul":
            mul_count += 1
            _mul(registers, parts[1], parts[2])
        elif instruction == "jnz":
            instruction_pointer = _jnz(instruction_pointer, registers, parts[1], parts[2])
            continue
        instruction_pointer += 1
    return mul_count


def find_value_left_in_register_h() -> int:
    # HARDCODED
    # DISCLAIMER: These values are specific to my input
    #
    # The program is a prime checker Checking which numbers between
    # registers b and c are not prime, in intervals of 17
    #
    # register b = 106500
    # register c = 123500
    #
    # Inspiration https://markheath.net/post/advent-of-code-2017-day-23

    h = 0
    for i in range(106500, 123501, 17):
        if not _is_prime(i):
            h += 1

    return h


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_times_mul_is_invoked(data)))
        print("Part 2: " + str(find_value_left_in_register_h()))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
