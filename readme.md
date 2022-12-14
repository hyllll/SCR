# Introduction
This is the code for Speech Conversation based Recommendation (SCR).

<!-- # Run -->
<!-- Please refer to this [document](https://fssntlo70a.feishu.cn/docx/ObVqdxPnZooShAxgpE1czsEKnHh) on how to run the code. -->
## Dataset
Download [ml-1m_thanks data](https://drive.google.com/file/d/1YZpuax0PrqtlNfyHGVkhDHdqFSn9MmHH/view?usp=sharing) from google drive and put it in `./Evaluate/data/ml-1m/`

## Installtion
Install dependencies via:
```
pip3 install -r requirements.txt
```

## Run
1. ```cd ./Evaluate/```
2.  Evaluate the quality of the dialogue:

    ```python3 evaluate.py --dataset='inspire' --eval_num=2000```

    ```python3 evaluate.py --dataset='ml-1m_thanks' --eval_num=2000```
    
    <!-- The `xxx` option are `inspire` and `ml-1m_thanks` -->
3. The results are saved in ```./Evaluate/res/```




