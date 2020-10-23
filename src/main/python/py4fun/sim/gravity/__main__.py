from py4fun.sim.gravity.sample import *
from py4fun.util import getorelse
import sys

if __name__ == "__main__":
    print(__package__)
    print(__name__)
    sample(getorelse(sys.argv, 1, "simulation"))
