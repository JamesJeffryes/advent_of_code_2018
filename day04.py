import time
from collections import defaultdict, Counter


def sort_events(filepath):
    with open(filepath) as infile:
        events = infile.readlines()
    events.sort(key=lambda x: time.strptime(x.split("]", 1)[0], '[%Y-%m-%d %H:%M'))
    return events


def parse_events(event_list):
    sleep_count = defaultdict(Counter)
    curr_guard = None
    asleep_min = None
    for event in event_list:
        timestamp, action = event.strip("[\n").split("] ", 1)
        _, curr_time = timestamp.split()
        hr, curr_min = curr_time.split(":")
        if "Guard" in action:
            if asleep_min:
                raise ValueError(f"{curr_guard} was asleep at shift change: {timestamp}")
            curr_guard = action.split()[1]
        elif action == "wakes up":
            if asleep_min is None:
                raise ValueError(f"Unexpected wake up at {timestamp}")
            for minute in range(int(asleep_min), int(curr_min)):
                sleep_count[curr_guard][minute] += 1
            asleep_min = None
        elif action == "falls asleep" and asleep_min is None:
            if asleep_min is not None or hr != "00":
                raise ValueError(f"Unexpected fall asleep at {timestamp}")
            asleep_min = curr_min
    return sleep_count


def strategy_one(sleep_count):
    total_sleep = Counter()
    for guard, sleep_mins in sleep_count.items():
        total_sleep[guard] = sum(sleep_mins.values())
    sleepiest_guard = total_sleep.most_common(1)[0][0]
    sleepiest_min = sleep_count[sleepiest_guard].most_common(1)[0][0]
    return sleepiest_guard, sleepiest_min, int(sleepiest_guard[1:])*sleepiest_min


def strategy_two(sleep_count):
    max_sleep = Counter()
    for guard, sleep_mins in sleep_count.items():
        max_sleep[guard] = sleep_mins.most_common(1)[0][1]
    sleepiest_guard = max_sleep.most_common(1)[0][0]
    sleepiest_min = sleep_count[sleepiest_guard].most_common(1)[0][0]
    return sleepiest_guard, sleepiest_min, int(sleepiest_guard[1:])*sleepiest_min


events = sort_events('inputs/04_1.txt')
parsed_events = parse_events(events)
print(strategy_one(parsed_events))
print(strategy_two(parsed_events))