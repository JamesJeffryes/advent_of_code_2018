import itertools

def sum_strings(path):
    freq = 0
    with open(path) as infile:
        for line in infile:
            freq += int(line)
    return freq

def duplicate_freq(path):
    freq = 0
    seen = {freq, }
    with open(path) as infile:
        for line in itertools.cycle(infile.readlines()):
            freq += int(line)
            if freq in seen:
                return freq
            seen.add(freq)

print(sum_strings('inputs/01_1.txt'))
print(duplicate_freq('inputs/01_1.txt'))