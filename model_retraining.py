'''
@Time : 2023-10-07 15:33
@Author : laolao
@FileName: data_preprocessing.py
'''
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import urllib
import pickle


def get_query_list(filename, tag):
    directory = str(os.getcwd())
    filepath = directory + "/" + filename
    data = open(filepath, 'r', encoding='gbk').readlines()
    query_list = []
    for d in data:
        d = str(urllib.parse.unquote(d))  # converting url encoded data to simple string
        query_list.append(d)
    _query_list = list(set(query_list))
    _y = [tag for i in range(0, len(_query_list))]
    return _query_list, _y


bad_query_list, bad_y = get_query_list('dta/nsfocus_isop.txt', 1)
good_query_list, good_y = get_query_list('data/goodqueries.txt', 0)
queries = bad_query_list + good_query_list
y = bad_y + good_y


def get_ngrams(query):
    tempQuery = str(query)
    ngrams = []
    for i in range(0, len(tempQuery) - 3):
        ngrams.append(tempQuery[i:i + 3])
    return ngrams


vectorizer = TfidfVectorizer(tokenizer=get_ngrams)
X = vectorizer.fit_transform(queries)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=20, random_state=42)

with open('lgs.pickle', 'rb') as input:
    w = pickle.load(input)
w.fit(X_train, y_train)
print('模型的准确度:{}'.format(w.score(X_test, y_test)))
with open('file/lgs_add_isop.pickle', 'wb') as output:
    pickle.dump(w, output)
