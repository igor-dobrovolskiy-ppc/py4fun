#!/bin/bash
source init.sh

echo ====== start ======

#PYTHONPATH=src/main/python python main.py
PYTHONPATH=src/main/python python -m py4fun.sim.gravity unbalanced_sun_sys

echo ====== end ========

source deinit.sh

open sun_system_sim.mp4

exit 0
