# Introduction
This is the code for Speech Conversation based Recommendation (SCR).

<!-- # Run -->
<!-- Please refer to this [document](https://fssntlo70a.feishu.cn/docx/ObVqdxPnZooShAxgpE1czsEKnHh) on how to run the code. -->
## Dataset
Download [ml-1m data](https://drive.google.com/file/d/163Q9v1u_mlTTzBWFzrBNIQLkbTcMwEM8/view?usp=share_link) from google drive and put it in `./Evaluate/data/ml-1m/`

## Installtion
Install dependencies via:
```
pip3 install -r requirements.txt
```

## Run
1. ```cd ./Evaluate/```
2.  Evaluate the quality of the dialogue:

    ```python3 evaluate.py --dataset='xxx' --eval_num=2000```
    
    The `xxx` option is `coat`, `ml-1m`, `opendialKG` and `redial`




