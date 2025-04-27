#!/bin/bash
#SBATCH --job-name="thSpread"
#SBATCH --output="job.%j.%N.out"
#SBATCH --partition=debug
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=8
#SBATCH -t 00:30:00
#SBATCH -A csd799

export OMP_NUM_THREADS=16
export OMP_PLACES=threads
export OMP_PROC_BIND=spread

source /home/imazalov/.bashrc

conda activate siesta

siesta Elec-Au-Top.fdf > Elec-Au-Top.out
