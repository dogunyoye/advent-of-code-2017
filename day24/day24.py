import copy
import os.path
import sys

DATA = os.path.join(os.path.dirname(__file__), 'day24.txt')


def __reverse(component) -> str:
    slash_idx = component.index("/")
    first, second = component[0:slash_idx], component[slash_idx + 1:]
    return second + "/" + first


def __can_connect(first, second) -> list:
    first_port = first[first.index("/") + 1:]
    second_port = second[0:second.index("/")]
    options = []

    if first_port == second_port:
        options.append(second)

    reverse_second = __reverse(second)
    reverse_second_port = reverse_second[0:reverse_second.index("/")]

    if first_port == reverse_second_port:
        options.append(reverse_second)

    return options


def __build_bridge(component, bridge, components, configs):
    if len(components) == 0:
        configs.append(bridge)
        return

    for i, c in enumerate(components):
        options = __can_connect(component, c)
        for o in options:
            bridge_copy, components_copy = copy.deepcopy(bridge), copy.deepcopy(components)
            bridge_copy.append(o)
            del components_copy[i]
            __build_bridge(o, bridge_copy, components_copy, configs)

    configs.append(bridge)


def __config_ports(config) -> list:
    ports = []
    for component in config:
        parts = component.split("/")
        ports.append(parts[0])
        ports.append(parts[1])
    return ports


def find_strongest_bridge(data) -> int:
    components = data.splitlines()
    configs = []
    strongest = -sys.maxsize - 1

    indices = []
    # optimisation
    # remove components with matching ports
    # they significantly increase the search
    # space and don't add value when searching
    # for valid configs
    for i, component in enumerate(components):
        parts = component.split("/")
        if parts[0] == parts[1]:
            indices.append(i)

    indices.reverse()
    symmetrical_components = {}

    # we store them in a map so that we can see
    # if they can be inserted in any generated
    # config
    for idx in indices:
        parts = components[idx].split("/")
        symmetrical_components[parts[0]] = int(parts[0]) * 2
        del components[idx]

    for i, component in enumerate(components):
        if component.startswith("0"):
            components_copy: list = copy.deepcopy(components)
            del components_copy[i]
            bridge = [component]
            __build_bridge(component, bridge, components_copy, configs)

    for config in configs:
        score = 0
        used = set()
        for component in config:
            parts = component.split("/")
            score += int(parts[0]) + int(parts[1])
            if parts[0] in symmetrical_components and parts[0] not in used:
                score += symmetrical_components[parts[0]]
                used.add(parts[0])
            elif parts[1] in symmetrical_components and parts[1] not in used:
                score += symmetrical_components[parts[1]]
                used.add(parts[1])
        strongest = max(strongest, score)

    return strongest


def find_strength_of_the_longest_bridge(data) -> int:
    components = data.splitlines()
    configs = []
    strongest, longest = -sys.maxsize - 1, -sys.maxsize - 1

    indices = []
    # optimisation
    # remove components with matching ports
    # they significantly increase the search
    # space and don't add value when searching
    # for valid configs
    for i, component in enumerate(components):
        parts = component.split("/")
        if parts[0] == parts[1]:
            indices.append(i)

    indices.reverse()
    symmetrical_components = {}

    # we store them in a map so that we can see
    # if they can be inserted in any generated
    # config
    for idx in indices:
        parts = components[idx].split("/")
        symmetrical_components[parts[0]] = int(parts[0]) * 2
        del components[idx]

    for i, component in enumerate(components):
        if component.startswith("0"):
            components_copy: list = copy.deepcopy(components)
            del components_copy[i]
            bridge = [component]
            __build_bridge(component, bridge, components_copy, configs)

    for config in configs:
        additional_components = 0
        ports = __config_ports(config)
        for k in symmetrical_components.keys():
            if k in ports:
                additional_components += 1

        config_length = len(config) + additional_components

        if config_length >= longest:
            longest = config_length
            score = 0
            used = set()
            for component in config:
                parts = component.split("/")
                score += int(parts[0]) + int(parts[1])
                if parts[0] in symmetrical_components and parts[0] not in used:
                    score += symmetrical_components[parts[0]]
                    used.add(parts[0])
                elif parts[1] in symmetrical_components and parts[1] not in used:
                    score += symmetrical_components[parts[1]]
                    used.add(parts[1])
            strongest = max(strongest, score)

    return strongest


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_strongest_bridge(data)))
        print("Part 2: " + str(find_strength_of_the_longest_bridge(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
