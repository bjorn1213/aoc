import numpy as np

map1 = [(0, np.inf, 0)]

map2 = [(98, 99, -48), (50, 97, 2)]


def merge_maps(map1, map2):
    it1 = iter(sorted(map1, key=lambda x: x[0]))
    it2 = iter(sorted(map2, key=lambda x: x[0]))

    def get_next(it):
        try:
            return next(it)
        except:
            return None

    rng1 = get_next(it1)
    rng2 = get_next(it2)

    new_maps = []

    prev_min = -np.inf

    while rng1 or rng2:
        if rng1 is None:
            lb, ub, delta = rng2
            rng2 = get_next(it2)
        elif rng2 is None:
            lb, ub, delta = rng1
            rng1 = get_next(it1)
        else:
            x = np.argmin([rng1[0], rng2[0]])
            y = np.argmin([rng1[1], rng2[1]])

            z = [rng1, rng2]
            lb = np.maximum(z[x][0], prev_min)
            ub = np.minimum(z[y][0], z[y][1])
            delta = rng1[2] + rng2[2]

            prev_min = lb + 1

            if y == 0:
                rng2 = (ub + 1, rng2[1], rng2[2])
                rng1 = get_next(it1)
            else:
                rng1 = (ub + 1, rng1[1], rng1[2])
                rng2 = get_next(it2)
        n = (lb, ub, delta)
        new_maps.append(n)

    return new_maps


map12 = merge_maps(map1, map2)

for m in map12:
    print(m)
print()
