import re, os, gensim, nltk
import pandas as pd
from pymorphy2 import MorphAnalyzer
from nltk.corpus import stopwords


def tokenize(files):
    vocabs = []
    tags = []
    stopwords_ru = stopwords.words("russian")
    morph = MorphAnalyzer()     
    
    for f in files:
        tags.append(f.split('/')[-1])
        file = open(f, 'r', encoding='utf-8')
        data = re.sub('[\d\W_a-zA-Z]+', ' ', file.read())
        data = data.lower()
        
        tokens = []
      
        for token in data.split():
            if token and token not in stopwords_ru:
                token = token.strip()
                token = morph.normal_forms(token)[0]
                if len(token) > 2:
                    tokens.append(token)
               
        vocabs.append(tokens[1:-1])
        
    return vocabs, tags

def tagged_document(vocabs, tags):
    for i in range(len(vocabs)):
        yield gensim.models.doc2vec.TaggedDocument(vocabs[i], [tags[i]])
        

if __name__ == "__main__":
    
    folder = $FOLDERPATH
 
    boted_files = []
    for i in range(100):
        boted_files.append(folder+'boted/bot'+str(i)+'.txt')
    
    human_files = []
    for i in range(100):
        human_files.append(folder+'human/human'+str(i)+'.txt')
    
    human_tokens, human_tags = tokenize(human_files)
    boted_tokens, boted_tags = tokenize(boted_files)
    
    data_tokens = human_tokens + boted_tokens
    data_tags = human_tags + boted_tags
    
    data_to_vectorize = list(tagged_document(data_tokens, data_tags))

    model = gensim.models.doc2vec.Doc2Vec(vector_size=40, min_count=2, epochs=30)
    model.build_vocab(data_to_vectorize)
    model.train(data_to_vectorize, total_examples=model.corpus_count, epochs=model.epochs)
    model.save('DostModel')

    vectors = []
    for tag in data_tags:
        clss = tag.split('.')[0]
        clss = re.sub('[\d]+', '', clss)
        vec = model.dv[model.dv.index_to_key.index(tag)]
        row = {'tag': tag, 'class': clss}
        for v in range(40):
            row['v'+str(v)] = vec[v]
        vectors.append(row)
        
    df = pd.DataFrame.from_dict(vectors)
    df.to_csv(folder+'vectors.csv')