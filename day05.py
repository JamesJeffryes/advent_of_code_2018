import string
import timeit
import time


def react(polymer):
    def _is_reactive(a, b):
        if a != b and a.lower() == b.lower():
            return True
        return False

    new_poly = []
    for x in polymer:
        if new_poly and _is_reactive(new_poly[-1], x):
            new_poly.pop()
        else:
            new_poly.append(x)
    return len(new_poly)

t1 = time.time()
with open("inputs/05.txt") as infile:
    polymer = infile.read().strip()

print(react(polymer))
for char in string.ascii_lowercase:
    filtered_poly = polymer.replace(char, "").replace(char.upper(), "")
    print(char, react(filtered_poly))

print("\nBenchmarking:")
print(time.time()-t1)
print(timeit.timeit(lambda: react(polymer), number=10)/10)
