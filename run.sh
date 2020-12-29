#!/bin/bash
source init.sh

echo ====== start ======

#PYTHONPATH=src/main/python python main.py
PYTHONPATH=src/main/python python -m py4fun.sim.gravity src/main/python/simulation

echo ====== end ========

source deinit.sh

type open
if ! [ $? ]; then
	open src/main/python/simulation.mp4
else	
	start src/main/python/simulation.mp4
fi

exit 0
