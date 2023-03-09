#!/bin/bash

## sbatch -p ex_batch --qos ex_gpu --gres=gpu:2 -c 40 tools/sbatch_train.sh
## sbatch -p batch_72h --qos gpu --gres=gpu:rtx2080:4 -c 40 -C "highcpucount" tools/sbatch_train.sh
## titanv, rtx2080

## TODO:
## 1) --job-name
## 2) --mail
## 3) --output
## 4) cmd

#SBATCH --job-name=revide
#SBATCH --mail-user=jqxu@cse.cuhk.edu.hk
#SBATCH --mail-type=ALL
#SBATCH --output=work_dirs/log_revide.txt  ##Do not use "~" point to your home!
##SBATCH --gres=gpu:1
#SBATCH --nodelist=gpu57

## Below is the commands to run , for this example,
## Create a sample helloworld.py and Run the sample python file
## Result are stored at your defined --output location


cd /research/dept6/jqxu/Projects/haze/mmediting &&
bash tools/dist_train.sh configs/dehazers/mapnet/mapnet_revide.py  2
