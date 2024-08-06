import os.path
import re

DATA = os.path.join(os.path.dirname(__file__), 'day07.txt')


def __build_structure(data) -> dict:
    structure = {}
    for line in data.splitlines():
        if "->" in line:
            parts = line.split(" -> ")
            parent_parts = parts[0].split(" ")
            name, weight = parent_parts[0], int(parent_parts[1].replace("(", "").replace(")", ""))

            children = []
            children_parts = parts[1].split(", ")
            for c in children_parts:
                children.append(c)
            structure[(name, weight)] = children
        else:
            parts = re.findall(r'([a-z]+) \((\d+)\)', line)[0]
            structure[(parts[0], int(parts[1]))] = []

    return structure


def __find_node(name, structure) -> tuple:
    for k, v in structure.items():
        if k[0] == name:
            return k
    raise Exception("Could not find node!")


def __dfs(start, structure, weights) -> int:
    node = __find_node(start, structure)
    children = structure[node]

    if len(children) == 0:
        weights[start] = node[1]
        return node[1]

    total = node[1]

    for c in children:
        total += __dfs(c, structure, weights)

    weights[start] = total
    return total


def __find_unbalanced_node(start, structure, weights) -> str:
    current_node = start

    while True:
        children = structure[__find_node(current_node, structure)]
        matches = 0
        for i, c in enumerate(children):
            match = False
            for j, cc in enumerate(children):
                if i == j:
                    continue
                if weights[c] == weights[cc]:
                    match = True
                    matches += 1
                    break

            if not match:
                current_node = c
                break

        if matches == len(children):
            return current_node


def find_name_of_bottom_program(data) -> str:
    structure = __build_structure(data)
    for k, v in structure.items():
        is_child = False
        for vv in structure.values():
            for c in vv:
                if c == k[0]:
                    is_child = True
                    break
        if not is_child:
            return k[0]

    raise Exception("Cannot find root!")


def find_balancing_weight(data) -> int:
    weights = {}
    structure = __build_structure(data)
    root = find_name_of_bottom_program(data)
    __dfs(root, structure, weights)

    root_children = structure[__find_node(root, structure)]
    result, dup = set(), 0
    for rc in root_children:
        if weights[rc] in result:
            dup = weights[rc]
        result.add(weights[rc])

    unbalanced = __find_unbalanced_node(root, structure, weights)

    result_list = sorted(list(result))
    balancing_weight = abs(result_list[0] - result_list[1])
    # Effectively means, if the unbalanced node is larger
    # than the other nodes, take weight away.
    if dup == result_list[0]:
        balancing_weight *= -1

    return __find_node(unbalanced, structure)[1] + balancing_weight


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + find_name_of_bottom_program(data))
        print("Part 2: " + str(find_balancing_weight(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
