#!/bin/bash
#SBATCH --job-name=JointFit2020
#SBATCH --output=SUBMITSCRIPTOUTPUT
#SBATCH --error=ERRORFILE
#SBATCH --partition=htc
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1 --constraint='gpu_gen:Kepler'
#SBATCH --time=5-0
#SBATCH --mem=16G

srun EXECUTABLENAME
