#!/bin/sh

### Set the job name (for your reference)
#PBS -N nlp_project
### Set the project name, your department code by default
#PBS -P cse
### Request email when job begins and ends
#PBS -m bea
### Specify email address to use for notification.
#PBS -M anz208486@iitd.ac.in
####
#PBS -l select=1:ncpus=2
### Specify "wallclock time" required for this job, hhh:mm:ss
#PBS -l walltime=10:05:00

# After job starts, must goto working directory. 
# $PBS_O_WORKDIR is the directory from where the job is fired. 
echo "==============================="
echo $PBS_JOBID
cat $PBS_NODEFILE
echo $PBS_O_WORKDIR
echo "==============================="
#job
source ~/anaconda3/etc/profile.d/conda.sh
conda activate /home/cse/phd/csz208507/anaconda3/envs/nlp_env
python3 /scratch/cse/phd/anz208486/col873_project/NLP_project/code/runscript_Estar.py
#NOTE
# The job line is an example : users need to change it to suit their applications
# The PBS select statement picks n nodes each having m free processors
# OpenMPI needs more options such as $PBS_NODEFILE
