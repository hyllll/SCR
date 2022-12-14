import fed
import json
import os
import time
import random
import argparse
import numpy as np
from collections import defaultdict


def load_data(dataset):
    with open(f"./data/{dataset}/dialogue_eval_{dataset}", "r") as fp:   
        data = json.load(fp)
    
    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='dialogue evaluate')
    parser.add_argument('--dataset', 
                        type=str, 
                        default='coat', 
                        help='select dataset, option: coat, ml-1m, opendialKG, redial, inspire')
    parser.add_argument('--eval_num', 
                        type=int, 
                        default=400, 
                        help='the number of dialogues')
    args = parser.parse_args()
    cur_time = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))[5:]
    data = load_data(args.dataset)
    model, tokenizer = fed.load_models("microsoft/DialoGPT-large")
    print("model load successful")

    scores = []
    if args.dataset != 'inspire':
        data = random.sample(data, args.eval_num)
    num = 0
    for conversation in data:
        scores.append(fed.evaluate(conversation, model, tokenizer))
        num += 1
        print("finish:", num)

    fed_scores = defaultdict(list)
    for result in scores:
        score_val = 0.0
        for key, val in result.items():
            fed_scores[key].append(val)
            score_val += val 
        fed_scores['fed_overall'].append(score_val / len(result))
    
    results = {}
    for metric, val in fed_scores.items():
        val = np.array(val)
        tmp = {}
        tmp['mean'] = np.mean(val)
        tmp['std'] = np.std(val)
        results[metric] = tmp

    save_dir = f'./res/{args.dataset}/'
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    with open(save_dir + f'{cur_time}_{args.dataset}_results.json', 'w') as f:
        json.dump(fed_scores, f)
