#!/bin/bash
#SBATCH --job-name=JointFit2020
#SBATCH --output=SUBMITSCRIPTOUTPUT
#SBATCH --error=ERRORFILE
#SBATCH --account=def-tanaka-ac
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:1
#SBATCH --time=5-0
#SBATCH --mem-per-cpu=4000M

srun EXECUTABLENAME
