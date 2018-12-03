import re
from collections import namedtuple, defaultdict


def parse_lines(filepath):
    swatch = namedtuple('swatch', ['id', 'x', 'y', 'w', 'h'])
    swatches = []
    with open(filepath) as infile:
        for line in infile:
            # extracts from : #123 @ 3,2: 5x4
            match = re.match("#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", line)
            swatches.append(swatch(*[int(x) for x in match.groups()]))
    return swatches


def get_clashes(swatch_list):
    clash_dict = defaultdict(int)
    for swatch in swatch_list:
        for x in range(swatch.x, swatch.x+swatch.w):
            for y in range(swatch.y, swatch.y+swatch.h):
                clash_dict[(x, y)] += 1

    return [coords for coords, count in clash_dict.items() if count > 1]


def get_no_clash(swatch_list, clash_coords):
    clash_coords = set(clash_coords)
    for swatch in swatch_list:
        if not _clashes(swatch, clash_coords):
            return swatch.id
    return None


def _clashes(swatch, coords):
    for x in range(swatch.x, swatch.x + swatch.w):
        for y in range(swatch.y, swatch.y + swatch.h):
            if (x, y) in coords:
                return True
    return False

swatches = parse_lines('inputs/03_1.txt')
clash_coords = get_clashes(swatches)
print(len(clash_coords))
print(get_no_clash(swatches, clash_coords))
