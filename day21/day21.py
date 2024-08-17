import os.path
import copy
from collections import Counter

DATA = os.path.join(os.path.dirname(__file__), 'day21.txt')


def print_image(image):
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    for i in range(0, limit):
        line = ""
        for j in range(0, limit):
            line += image[(i, j)]
        print(line)


def flip(image) -> dict:
    flipped = {}
    lines = []
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    for i in range(limit - 1, -1, -1):
        line = ""
        for j in range(0, limit):
            line += image[(i, j)]
        lines.append(line)

    for i, line in enumerate(lines):
        for j in range(0, len(line)):
            flipped[(i, j)] = line[j]

    return flipped


def rotate(image) -> dict:
    rotated = {}
    lines = []
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    for i in range(0, limit):
        line = ""
        for j in range(0, limit):
            line += image[(j, i)]
        lines.append(list(reversed(line)))

    for i, line in enumerate(lines):
        for j in range(0, len(line)):
            rotated[(i, j)] = line[j]

    return rotated


def transformations(image) -> list:
    transforms = [copy.deepcopy(image)]
    for _ in range(0, 3):
        image = rotate(image)
        transforms.append(copy.deepcopy(image))

    image = flip(rotate(image))
    transforms.append(copy.deepcopy(image))

    for _ in range(0, 3):
        image = rotate(image)
        transforms.append(copy.deepcopy(image))

    return transforms


def __split_image(image) -> (list, int):
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    if limit == 2 or limit == 3:
        return [image], 1

    images = []
    step = 0
    if limit % 2 == 0:
        step = 1
    elif limit % 3 == 0:
        step = 2

    bounds = []
    for i in range(0, limit, step + 1):
        bounds.append((i, i + step))

    for i in bounds:
        for j in bounds:
            split_image = {}
            for i_idx, ii in enumerate(range(i[0], i[1] + 1)):
                for j_idx, jj in enumerate(range(j[0], j[1] + 1)):
                    split_image[(i_idx, j_idx)] = image[(ii, jj)]
            images.append(split_image)
    return images, len(bounds)


def __merge_images(images, rows) -> dict:
    if len(images) == 1:
        return images[0]

    lines, split_lines = [], []
    merged = {}
    limit = max(images[0].keys(), key=lambda item: item[1])[1] + 1

    for i in range(0, len(images), rows):
        row = images[i:i + rows]
        for depth in range(0, limit):
            line = ""
            for image in row:
                for width in range(0, limit):
                    line += image[(depth, width)]
            lines.append(line)

    for i, line in enumerate(lines):
        for j in range(0, len(line)):
            merged[(i, j)] = line[j]

    return merged


def __build_image(input_data) -> dict:
    image = {}
    for i, line in enumerate(input_data.split("/")):
        for j in range(0, len(line)):
            image[(i, j)] = line[j]
    return image


def __image_string(image) -> str:
    image_string = ""
    limit = max(image.keys(), key=lambda item: item[1])[1] + 1
    for i in range(0, limit):
        for j in range(0, limit):
            image_string += image[(i, j)]
    return image_string


def __enhancement_map(data) -> dict:
    replacements = {}
    for line in data.splitlines():
        parts = line.split(" => ")
        replacements[parts[0].replace("/", "")] = __build_image(parts[1])
    return replacements


def __create_initial_image() -> dict:
    initial_image = {(0, 0): '.', (0, 1): '#', (0, 2): '.',
                     (1, 0): '.', (1, 1): '.', (1, 2): '#',
                     (2, 0): '#', (2, 1): '#', (2, 2): '#'}
    return initial_image


# Trivial for part 1, slow for part 2 (but will complete in a reasonable
# enough time). Possibly a trick here to get an answer quicker.
def __number_of_pixels_on_after_n_iterations(data, iterations) -> int:
    image = __create_initial_image()
    enhancements = __enhancement_map(data)

    while iterations != 0:
        subsections = []
        split_image, rows = __split_image(image)
        for s in split_image:
            found = False
            for tt in transformations(s):
                sub_image_string = __image_string(tt)
                if sub_image_string in enhancements:
                    subsections.append(enhancements[sub_image_string])
                    found = True
                    break

            if not found:
                raise Exception("Enhancement not found!")

        image = __merge_images(subsections, rows)
        iterations -= 1

    return Counter(image.values())['#']


def find_number_of_pixels_on_after_five_iterations(data) -> int:
    return __number_of_pixels_on_after_n_iterations(data, 5)


def find_number_of_pixels_on_after_eighteen_iterations(data) -> int:
    return __number_of_pixels_on_after_n_iterations(data, 18)


def main() -> int:
    with open(DATA) as f:
        data = f.read()
        print("Part 1: " + str(find_number_of_pixels_on_after_five_iterations(data)))
        print("Part 2: " + str(find_number_of_pixels_on_after_eighteen_iterations(data)))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
