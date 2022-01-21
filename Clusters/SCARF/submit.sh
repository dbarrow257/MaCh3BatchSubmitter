#!/bin/bash
#SBATCH --job-name=JointFit2020
#SBATCH --output=SUBMITSCRIPTOUTPUT
#SBATCH --error=ERRORFILE
#SBATCH --partition=gpu
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --time=5-0
#SBATCH --mem=16G

srun EXECUTABLENAME
