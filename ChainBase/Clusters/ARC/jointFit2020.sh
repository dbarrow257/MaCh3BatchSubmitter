#!/bin/bash

source /home/magd5023/.sourceMeForMaCh3
cd /data/phys-t2k/magd5023/M3-2020/MaCh3/
source /data/phys-t2k/magd5023/M3-2020/MaCh3/setup.sh
export OMP_NUM_THREADS=8

./bin/jointFit2020 CONFIGNAME > CONSOLELOG
