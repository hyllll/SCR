import json
import pandas as pd
import re
import argparse

def coat_loader():
    with open("./data/coat/dialogue_info.json",'r') as load_f:
        coat = json.load(load_f)
    contexts = []
    for _, dialogue in coat.items():
        dialogue_content = dialogue["content"]
        context = []
        for _, text in dialogue_content.items():
            context.append(text)
        context = ' <|endoftext|> '.join(context)
        context = '<|endoftext|> ' + context + ' <|endoftext|>'
        contexts.append(context)
    
    return contexts

def movie_loader():
    with open("./data/movie/dialogue_info.json",'r') as load_f:
        movie = json.load(load_f)
    contexts = []
    for _, dialogue in movie.items():
        dialogue_content = dialogue["content"]
        context = []
        for _, text in dialogue_content.items():
            context.append(text)
        context = ' <|endoftext|> '.join(context)
        context = '<|endoftext|> ' + context + ' <|endoftext|>'
        contexts.append(context)
    
    return contexts

def redial_loader():
    train_data = []
    for line in open("./data/redial/train_data.jsonl", "r"):
        train_data.append(json.loads(line))
    movie = pd.read_csv("./data/redial/movies_with_mentions.csv")
    contexts = []
    for data in train_data:
        context = []
        message = data['messages']
        for text in message:
            text = text['text']
            text = text.split(' ')
            word_dict = {}
            for index, word in enumerate(text):
                if '@' in word:
                    # print(word)
                    movie_Id = word.split('@')[1]
                    if (movie_Id == '') or (not bool(re.search(r'\d', movie_Id))):
                        continue
                    movie_Id = int(re.findall("\d+",movie_Id)[0])
                    movie_name = list(movie[movie['movieId'] == movie_Id]['movieName'])[0]
                    movie_name = movie_name.split('(')[0].strip()
                    text[index] = movie_name
            text = ' '.join(text)
            context.append(text)
        context = ' <|endoftext|> '.join(context)
        context = '<|endoftext|> ' + context + ' <|endoftext|>'
        contexts.append(context)

        return contexts

def opendialKG_loader():
    data = pd.read_csv("./data/opendialKG/opendialkg.csv")
    attr = ['book', 'books', 'Book', 'Books', 'books,', 'book,', 'books?', 'book?', 'book.', 'books.', 'author', 'authors', 'title', 'titles']
    attr = set(attr)
    index_list = []
    count = 0
    for index, row in data.iterrows():
        message = row['Messages']
        message = json.loads(message)
        tag = 0
        for m in message:
            if 'message' in m.keys():
                text = m['message']
                text = text.split(' ')
                if (attr & set(text)) and tag == 0:
                    count = count + 1
                    index_list.append(index)
                    tag = 1
    contexts = []
    for index, row in data.iterrows():
        if index in index_list:
            message = row['Messages']
            message = json.loads(message)
            context = []
            for m in message:
                if 'message' in m.keys():
                    context.append(m['message'])
            context = ' <|endoftext|> '.join(context)
            context = '<|endoftext|> ' + context + ' <|endoftext|>'
            contexts.append(context)
    
    return contexts

loader_dict = {
    'coat': coat_loader,
    'ml-1m': movie_loader,
    'redial': redial_loader,
    'opendialKG': opendialKG_loader
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='dialogue evaluate')
    parser.add_argument('--dataset', 
                        type=str, 
                        default='coat', 
                        help='select dataset, option: coat, ml-1m, opendialKG, redial')
    args = parser.parse_args()
    data = loader_dict[args.dataset]()
    with open(f"./data/{args.dataset}/dialogue_eval_{args.dataset}", "w") as fp:
        json.dump(data, fp)
    
    # with open("./data/coat/dialogue_eval", "r") as fp:   
    #     data = json.load(fp)
    
    # print(data[1])




