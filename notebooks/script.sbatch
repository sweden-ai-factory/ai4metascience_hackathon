#!/bin/bash
#SBATCH --job-name=metascience
#SBATCH --account=project_465002387
#SBATCH --partition=small-g
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus-per-task=1
#SBATCH --mem=60G
#SBATCH --time=2:00:00

# Load LUMI environment
module purge
module use /appl/local/laifs/modules
module load lumi-aif-singularity-bindings

# Container and project paths
export SIF=/appl/local/laifs/containers/lumi-multitorch-u24r70f21m50t210-20260807_115122/lumi-multitorch-full-u24r70f21m50t210-20260807_115122.sif

export STORAGE=/pfs/lustrep4/scratch/project_465002387/$USER/ai4metascience_hackathon/

# GPU cache
mkdir -p $STORAGE/miopen-cache
export MIOPEN_USER_DB_PATH=$STORAGE/miopen-cache
export MIOPEN_CUSTOM_CACHE_DIR=$STORAGE/miopen-cache

# Run hackathon application
srun singularity run "$SIF" bash -c "
# source $STORAGE/my-env/bin/activate &&
python3 sample.py
"