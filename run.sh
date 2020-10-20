#!/bin/bash
source init.sh

#PYTHONPATH=src/main/python python -v -m py4fun
PYTHONPATH=src/main/python python -m py4fun .

source deinit.sh

exit 0
