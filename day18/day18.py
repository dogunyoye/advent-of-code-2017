import os.path
from collections import deque

DATA = os.path.join(os.path.dirname(__file__), 'day18.txt')
last_played = 0


class Program(object):

    def __init__(self, registers, instructions):
        self.registers = registers
        self.instructions = instructions
        self.instruction_pointer = 0
        self.queue = deque()
        self.sent = 0

    def execute_program(self, other_program):
        while self.instruction_pointer < len(self.instructions):
            parts = self.instructions[self.instruction_pointer].split(" ")
            instruction = parts[0]
            if instruction == "snd":
                self.sent += 1
                other_program.queue.append(self.registers[parts[1]])
            elif instruction == "rcv":
                if len(self.queue) == 0:
                    return
                self.registers[parts[1]] = self.queue.popleft()
            elif instruction == "set":
                _set(self.registers, parts[1], parts[2])
            elif instruction == "add":
                _add(self.registers, parts[1], parts[2])
            elif instruction == "mul":
                _mul(self.registers, parts[1], parts[2])
            elif instruction == "mod":
                _mod(self.registers, parts[1], parts[2])
            elif instruction == "jgz":
                self.instruction_pointer = (
                    _jgz(self.instruction_pointer, len(self.instructions), self.registers, parts[1], parts[2]))
                continue
            self.instruction_pointer += 1
        raise Exception("Program out of bounds")


def _snd(registers, value):
    global last_played
    last_played = registers[value]


def _set(registers, register, value):
    if value.isalpha():
        registers[register] = registers[value]
        return
    registers[register] = int(value)


def _add(registers, register, value):
    if value.isalpha():
        registers[register] += registers[value]
        return
    registers[register] += int(value)


def _mul(registers, register, value):
    if value.isalpha():
        registers[register] *= registers[value]
        return
    registers[register] *= int(value)


def _mod(registers, register, value):
    if value.isalpha():
        registers[register] %= registers[value]
        return
    registers[register] %= int(value)


def _rcv() -> int:
    global last_played
    return last_played


def _jgz(instruction_pointer, instructions_len, registers, value0, value1) -> int:
    if value0.isalpha():
        v0 = registers[value0]
    else:
        v0 = int(value0)

    if value1.isalpha():
        v1 = registers[value1]
    else:
        v1 = int(value1)

    if v0 > 0:
        return instruction_pointer + v1
    return instruction_pointer + 1


def __initialise_registers(data) -> dict:
    registers = {}
    for line in data.splitlines():
        parts = line.split(" ")
        for i in range(1, len(parts)):
            if str(parts[i]).isalpha():
                registers[parts[i]] = 0
    return registers


def find_value_of_recovered_frequency(data) -> int:
    registers = __initialise_registers(data)
    instructions = data.splitlines()
    instruction_pointer = 0
    while instruction_pointer < len(instructions):
        parts = instructions[instruction_pointer].split(" ")
        instruction = parts[0]
        if instruction == "snd":
            _snd(registers, parts[1])
        elif instruction == "rcv":
            if registers[parts[1]] != 0:
                return _rcv()
        elif instruction == "set":
            _set(registers, parts[1], parts[2])
        elif instruction == "add":
            _add(registers, parts[1], parts[2])
        elif instruction == "mul":
            _mul(registers, parts[1], parts[2])
        elif instruction == "mod":
            _mod(registers, parts[1], parts[2])
        elif instruction == "jgz":
            instruction_pointer = _jgz(instruction_pointer, len(instructions), registers, parts[1], parts[2])
            continue
        instruction_pointer += 1

    return 0


def find_number_of_times_program_one_sent_a_value(data) -> int:
    program0_registers = __initialise_registers(data)
    program1_registers = __initialise_registers(data)

    program0_registers['p'] = 0
    program1_registers['p'] = 1

    program0: Program = Program(program0_registers, data.splitlines())
    program1: Program = Program(program1_registers, data.splitlines())

    while True:
        program0.execute_program(program1)
        program1.execute_program(program0)

        if len(program0.queue) == 0 and len(program1.queue) == 0:
            return program1.sent


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_value_of_recovered_frequency(data)))
        print("Part 2: " + str(find_number_of_times_program_one_sent_a_value(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
