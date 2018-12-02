from collections import Counter
import difflib


def count_boxes(box_ids):
    dup_count = Counter()
    for box in box_ids:
        letter_count = Counter(box)
        counts = set(letter_count.values())
        for count in counts:
            dup_count[count] += 1
    return dup_count[2] * dup_count[3]


def get_closest_match(box_ids):
    threshold = (len(box_ids[0])-1)/len(box_ids[0])
    for box in box_ids:
        matches = difflib.get_close_matches(box, box_ids, cutoff=threshold)  # stdlib FTW!
        if len(matches) > 1:  # we expect it to match itself
            return "".join([char for i, char in enumerate(matches[0]) if char == matches[1][i]])


boxes = [x.strip() for x in open('inputs/02_1.txt').readlines()]
print(count_boxes(boxes))
print(get_closest_match(boxes))