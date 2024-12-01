from pathlib import Path
import numpy as np

dirpath = Path("day5")
fname = dirpath / "day5.txt"
# fname = dirpath / "day5_small.txt"

with open(fname, "r") as f:
    lines = f.readlines()


def get_mapping_dict(src_start, dst_start, number):
    d = {}
    for i, j in zip(
        range(src_start, src_start + number), range(dst_start, dst_start + number)
    ):
        d[i] = j
    return d


class MappingClass:
    def __init__(self):
        self.maps = {}

    def add_range(self, start, length, delta):
        def f(key):
            if start <= key < start + length:
                return key + delta
            else:
                return key

        self.maps[start] = f

    def __getitem__(self, key):
        available_ranges = list(self.maps.keys())
        applicable = [r for r in available_ranges if r < key]
        if len(applicable) == 0:
            return key
        r = max(applicable)
        return self.maps[r](key)


seed2soil = MappingClass()
soil2fert = MappingClass()
fert2wat = MappingClass()
wat2light = MappingClass()
light2temp = MappingClass()
temp2hum = MappingClass()
hum2loc = MappingClass()

input_map = {
    "seed-to-soil map:": seed2soil,
    "soil-to-fertilizer map:": soil2fert,
    "fertilizer-to-water map:": fert2wat,
    "water-to-light map:": wat2light,
    "light-to-temperature map:": light2temp,
    "temperature-to-humidity map:": temp2hum,
    "humidity-to-location map:": hum2loc,
}

seeds = set()
active_map = input_map["seed-to-soil map:"]

for line in lines:
    l = line.replace("\n", "")

    if "seeds:" in l:
        _, l = l.split(":")
        seeds = set([int(s) for s in l.split(" ") if s != ""])
    elif l == "":
        continue
    elif not l[0].isnumeric():
        key = l
    else:
        dst_start, src_start, length = [int(x) for x in l.split(" ")]
        input_map[key].add_range(src_start, length, dst_start - src_start)

loc = np.inf
for seed in seeds:
    val = seed
    val = input_map["seed-to-soil map:"][val]
    val = input_map["soil-to-fertilizer map:"][val]
    val = input_map["fertilizer-to-water map:"][val]
    val = input_map["water-to-light map:"][val]
    val = input_map["light-to-temperature map:"][val]
    val = input_map["temperature-to-humidity map:"][val]
    val = input_map["humidity-to-location map:"][val]
    loc = min(loc, val)

print(loc)
