import copy
import os.path
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), 'day21.txt')


def _print_image(image):
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    for i in range(limit):
        line = ""
        for j in range(limit):
            line += image[(i, j)]
        print(line)


def _flip(image) -> dict:
    flipped = {}
    lines = []
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    for i in range(limit - 1, -1, -1):
        line = ""
        for j in range(limit):
            line += image[(i, j)]
        lines.append(line)

    for i, line in enumerate(lines):
        for j in range(len(line)):
            flipped[(i, j)] = line[j]

    return flipped


def _rotate(image) -> dict:
    rotated = {}
    lines = []
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    for i in range(limit):
        column = ""
        for j in range(limit):
            column += image[(j, i)]
        lines.append(list(reversed(column)))

    for i, line in enumerate(lines):
        for j in range(len(line)):
            rotated[(i, j)] = line[j]

    return rotated


def _transformations(image) -> list:
    transforms = [copy.deepcopy(image)]
    for _ in range(3):
        image = _rotate(image)
        transforms.append(copy.deepcopy(image))

    image = _flip(_rotate(image))
    transforms.append(copy.deepcopy(image))

    for _ in range(3):
        image = _rotate(image)
        transforms.append(copy.deepcopy(image))

    return transforms


def _split_image(image) -> tuple[list, int]:
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    if limit == 2 or limit == 3:
        return [image], 1

    images = []
    step = 0
    if limit % 2 == 0:
        step = 1
    elif limit % 3 == 0:
        step = 2

    bounds = [(i, i + step) for i in range(0, limit, step + 1)]

    for row_bounds in bounds:
        for column_bounds in bounds:
            split_image = {}
            for i_idx, ii in enumerate(range(row_bounds[0], row_bounds[1] + 1)):
                for j_idx, jj in enumerate(range(column_bounds[0], column_bounds[1] + 1)):
                    split_image[(i_idx, j_idx)] = image[(ii, jj)]
            images.append(split_image)
    return images, len(bounds)


def _merge_images(images, rows) -> dict:
    if len(images) == 1:
        return images[0]

    lines = []
    merged = {}
    limit = max(images[0].keys(), key=lambda item: item[1])[1] + 1

    for i in range(0, len(images), rows):
        row = images[i:i + rows]
        for depth in range(limit):
            line = ""
            for image in row:
                for width in range(limit):
                    line += image[(depth, width)]
            lines.append(line)

    for i, line in enumerate(lines):
        for j in range(len(line)):
            merged[(i, j)] = line[j]

    return merged


def _build_image(input_data) -> dict:
    image = {}
    for i, line in enumerate(input_data.split("/")):
        for j in range(len(line)):
            image[(i, j)] = line[j]
    return image


def _image_string(image) -> str:
    image_string = ""
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    for i in range(limit):
        for j in range(limit):
            image_string += image[(i, j)]
    return image_string


def _enhancement_map(data) -> dict:
    replacements = {}
    for line in data.splitlines():
        parts = line.split(" => ")
        replacements[parts[0].replace("/", "")] = _build_image(parts[1])
    return replacements


def _create_initial_image() -> dict:
    return {(0, 0): '.', (0, 1): '#', (0, 2): '.',
            (1, 0): '.', (1, 1): '.', (1, 2): '#',
            (2, 0): '#', (2, 1): '#', (2, 2): '#'}


# Trivial for part 1, slow for part 2 (but will complete in a reasonable
# enough time). Possibly a trick here to get an answer quicker.
def _number_of_pixels_on_after_n_iterations(data, iterations) -> int:
    image = _create_initial_image()
    enhancements = _enhancement_map(data)

    while iterations != 0:
        subsections = []
        split_image, rows = _split_image(image)
        for s in split_image:
            found = False
            for tt in _transformations(s):
                sub_image_string = _image_string(tt)
                if sub_image_string in enhancements:
                    subsections.append(enhancements[sub_image_string])
                    found = True
                    break

            if not found:
                raise ValueError("Enhancement not found!")

        image = _merge_images(subsections, rows)
        iterations -= 1

    return Counter(image.values())['#']


def find_number_of_pixels_on_after_five_iterations(data) -> int:
    return _number_of_pixels_on_after_n_iterations(data, 5)


def find_number_of_pixels_on_after_eighteen_iterations(data) -> int:
    return _number_of_pixels_on_after_n_iterations(data, 18)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_pixels_on_after_five_iterations(data)))
        print("Part 2: " + str(find_number_of_pixels_on_after_eighteen_iterations(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
