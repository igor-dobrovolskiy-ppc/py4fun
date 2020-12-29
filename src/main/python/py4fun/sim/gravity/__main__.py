from py4fun.sim.gravity.sample import *
from py4fun.util import getorelse
from functools import reduce
import sys

if __name__ == "__main__":
    print(__package__)
    print(__name__)
    t = (1, "a")
    print(t[1])
    d = {}

    def red_func(d: dict, kv: tuple) -> dict:
        if kv[0] not in d:
            d[kv[0]] = kv[1]
        else:
            d[kv[0]] = d[kv[0]] + kv[1]
        return d

    s = "a b c d b e a d e e"

    m = reduce(lambda i, kv: red_func(i, kv), [(e, 1) for e in s.split(' ')], d)

    print(m)

    l = [k*n for (k, n) in m.items()]

    print(l)

#    exit(0)

    sample(getorelse(sys.argv, 1, "simulation"))
