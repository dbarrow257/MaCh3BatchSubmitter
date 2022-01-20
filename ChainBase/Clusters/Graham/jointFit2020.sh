#!/bin/bash

source /home/barrow/.sourceMeForMaCh3
cd /scratch/barrow/M3-2020/MaCh3
source /scratch/barrow/M3-2020/MaCh3/setup.sh
export OMP_NUM_THREADS=16

./bin/jointFit2020 CONFIGNAME > CONSOLELOG
