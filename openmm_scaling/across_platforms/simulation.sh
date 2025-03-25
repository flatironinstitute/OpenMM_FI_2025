#!/bin/sh
#SBATCH -p gpu
#SBATCH -n 1
#SBATCH --gpus-per-node=3
#SBATCH --cpus-per-gpu=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=0-00:15:00

module purge
module load modules/2.3-20240529 cuda/12.3.2
source ~/openmm-env/bin/activate

python compare_large.py
#python run_from_chkpt.py

