#!/bin/bash

source /home/vol02/scarf932/.sourceMeForMaCh3
cd /home/vol02/scarf932/M3-2020/MaCh3-4May/
source /home/vol02/scarf932/M3-2020/MaCh3-4May/setup.sh
export OMP_NUM_THREADS=8

./bin/jointFit2020 CONFIGNAME > CONSOLELOG
