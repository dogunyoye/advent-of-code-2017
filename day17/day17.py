import os.path

DATA = os.path.join(os.path.dirname(__file__), 'day17.txt')


def find_value_after_2017(data) -> int:
    spins = int(data)
    state = [0]
    number = 1
    insertion_point = 0

    while number != 2018:
        insertion_point = ((insertion_point + spins) % len(state)) + 1
        if insertion_point >= len(state):
            state.append(number)
        else:
            state.insert(insertion_point, number)
        number += 1

    return state[state.index(2017) + 1]


def find_number_after_value_zero_when_fifty_million_is_inserted(data) -> int:
    spins = int(data)
    state = [0]
    number = 1
    insertion_point = 0

    # Modifying an array of 50M elements would be time-consuming
    # so let's not do that...
    #
    # Instead, we use the fact that value 0 never changes its
    # position (index 0) to our advantage.
    #
    # Based on this we only ever need to track what value is at
    # index 1. We're no longer constrained by the confines of the
    # buffer, every new number will increase the size of it. So all
    # we care about is which position (insertion_point) every number
    # ends up in. Ofcourse, we're not actually going to store every
    # number, just whatever number is at index 0 (always 0) and index 1
    while number != 50_000_000:
        insertion_point = ((insertion_point + spins) % number) + 1
        if insertion_point == 1:
            if insertion_point >= len(state):
                state.append(number)
            else:
                state[insertion_point] = number
        number += 1
    return state[1]


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_value_after_2017(data)))
        print("Part 2: " + str(find_number_after_value_zero_when_fifty_million_is_inserted(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
