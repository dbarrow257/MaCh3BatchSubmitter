#!/bin/bash                                                                                                                                                                                                 
source /opt/ppd/t2k/users/barrowd/RTX/M3-2020/MaCh3/sourceMeForMaCh3.sh
cd /opt/ppd/t2k/users/barrowd/RTX/M3-2020/MaCh3/
source /opt/ppd/t2k/users/barrowd/RTX/M3-2020/MaCh3/setup.sh
export OMP_NUM_THREADS=8

./bin/jointFit2020 CONFIGNAME > CONSOLELOG

