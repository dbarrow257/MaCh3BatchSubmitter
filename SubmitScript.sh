#!/bin/bash
#SBATCH --job-name=JOBNAME
#SBATCH --output=SUBMITSCRIPTOUTPUT
#SBATCH --error=ERRORFILE
#SBATCH --account=rpp-blairt2k
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:1
#SBATCH --time=3-0
#SBATCH --mem-per-cpu=4000M

srun EXECUTABLENAME
