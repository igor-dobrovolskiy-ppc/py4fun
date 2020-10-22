#!/bin/bash
source init.sh

echo ====== start ======

#PYTHONPATH=src/main/python python main.py
PYTHONPATH=src/main/python python -m py4fun.sim.gravity

echo ====== end ========

source deinit.sh

exit 0
