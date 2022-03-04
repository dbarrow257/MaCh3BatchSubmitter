#!/bin/bash

cd MACH3INSTALL
source setup.sh
export OMP_NUM_THREADS=NTHREADS

#INSERTJOB

while jobs %%;
do
  sleep 10
done
