#!/bin/bash

cd ./Evaluate/
if [ ! -f ./data/ml-1m/dialogue_eval_ml-1m ];
then
    cd ./data/ml-1m/
    gdown --id 1PLYag_DVKf5nebnwwfN0HG9OyeI-igtF
    cd ../../
fi
for((i=1;i<=5;i++));
do
python3 evaluate.py --dataset='coat' --eval_num=400
python3 evaluate.py --dataset='redial' --eval_num=400
python3 evaluate.py --dataset='opendialKG' --eval_num=400
python3 evaluate.py --dataset='ml-1m' --eval_num=2000
done
