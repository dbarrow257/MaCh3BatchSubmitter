#!/bin/bash
#SBATCH --job-name=JOBNAME
#SBATCH --output=SUBMITSCRIPTOUTPUT
#SBATCH --error=ERRORFILE
#SBATCH --account=rpp-blairt2k
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:v100l:1
#SBATCH --time=2:59:00
#SBATCH --mem=20G
#SBATCH --array=ARRAY

srun EXECUTABLENAME
