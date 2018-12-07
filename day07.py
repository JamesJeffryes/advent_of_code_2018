from copy import copy
import re
import string
from collections import defaultdict


def parse_input(filename):
    has_deps = defaultdict(set)
    is_dep_for = defaultdict(set)
    with open(filename) as infile:
        for line in infile:
            m = re.match('^Step (\w) must be finished before step (\w) can begin.$', line)
            prereq, step = m.groups()
            has_deps[step].add(prereq)
            is_dep_for[prereq].add(step)
    return has_deps, is_dep_for


def find_path(has_deps, is_dep_for):
    path = []
    next_node = [char for char in string.ascii_uppercase if char not in has_deps]
    while next_node:
        node = next_node.pop(0)
        path.append(node)
        for edge in is_dep_for[node]:
            has_deps[edge].remove(node)
            if not has_deps[edge]:
                next_node.append(edge)
        next_node.sort()
    return "".join(path)


def _step_time(step):
    return string.ascii_uppercase.index(step) + 61


def worktime(has_deps, is_dep_for, workers=5):
    def _fill_in_progress():
        while next_node and len(in_progress) < workers:
            node = next_node.pop(0)
            in_progress.append((time+_step_time(node), node))
        in_progress.sort()

    path = []
    in_progress = []
    next_node = [char for char in string.ascii_uppercase if char not in has_deps]
    time = 0
    _fill_in_progress()
    while in_progress:
        time, node = in_progress.pop(0)
        path.append(node)
        for edge in is_dep_for[node]:
            has_deps[edge].remove(node)
            if not has_deps[edge]:
                next_node.append(edge)
        next_node.sort()
        _fill_in_progress()
    return "".join(path), time


has_deps, is_dep_for = parse_input('inputs/07.txt')
print(worktime(has_deps, is_dep_for))
