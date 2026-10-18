import os.path
import sys

DATA = os.path.join(os.path.dirname(__file__), 'day24.txt')


def _reverse(component) -> str:
    slash_idx = component.index("/")
    first, second = component[0:slash_idx], component[slash_idx + 1:]
    return second + "/" + first


def _can_connect(first, second) -> list:
    first_port = first[first.index("/") + 1:]
    second_port = second[0:second.index("/")]
    options = []

    if first_port == second_port:
        options.append(second)

    reverse_second = _reverse(second)
    reverse_second_port = reverse_second[0:reverse_second.index("/")]

    if first_port == reverse_second_port:
        options.append(reverse_second)

    return options


def _build_bridge(component, bridge, components, used, configs):
    if len(used) == len(components):
        configs.append(list(bridge))
        return

    for i, c in enumerate(components):
        if i in used:
            continue
        for o in _can_connect(component, c):
            bridge.append(o)
            used.add(i)
            _build_bridge(o, bridge, components, used, configs)
            used.discard(i)
            bridge.pop()

    configs.append(list(bridge))


def _config_ports(config) -> list:
    ports = []
    for component in config:
        parts = component.split("/")
        ports.append(parts[0])
        ports.append(parts[1])
    return ports


def _all_configs(data) -> tuple[list, dict]:
    components = data.splitlines()
    configs: list = []

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
            remaining = components[:i] + components[i + 1:]
            _build_bridge(component, [component], remaining, set(), configs)

    return configs, symmetrical_components


def _config_score(config, symmetrical_components) -> int:
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
    return score


def find_strongest_bridge(data) -> int:
    configs, symmetrical_components = _all_configs(data)

    strongest = -sys.maxsize - 1
    for config in configs:
        strongest = max(strongest, _config_score(config, symmetrical_components))

    return strongest


def find_strength_of_the_longest_bridge(data) -> int:
    configs, symmetrical_components = _all_configs(data)

    strongest, longest = -sys.maxsize - 1, -sys.maxsize - 1
    for config in configs:
        additional_components = sum(
            1 for k in symmetrical_components if k in _config_ports(config))
        config_length = len(config) + additional_components

        if config_length >= longest:
            longest = config_length
            strongest = max(strongest, _config_score(config, symmetrical_components))

    return strongest


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_strongest_bridge(data)))
        print("Part 2: " + str(find_strength_of_the_longest_bridge(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
