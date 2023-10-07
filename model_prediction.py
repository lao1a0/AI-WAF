'''
@Time : 2023-10-07 15:51
@Author : laolao
@FileName: model_prediction.py
'''

from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import html

with open('file/lgs.pickle', 'rb') as input:
    w = pickle.load(input)

with open("data/nsfocus_isop.txt", "r") as f:
    my_code = f.readlines()


def get_ngrams(query):
    tempQuery = str(query)
    ngrams = []
    for i in range(0, len(tempQuery) - 3):
        ngrams.append(tempQuery[i:i + 3])
    return ngrams


vectorizer = TfidfVectorizer(tokenizer=get_ngrams)
print(my_code)
X_predict = vectorizer.transform(my_code)
res = w.predict(X_predict)
res_list = []
for q, r in zip(my_code, res):
    tmp = '正常请求' if r == 0 else '恶意请求'
    # print('{}  {}'.format(q,tmp))
    q_entity = html.escape(q)
    res_list.append({'url': q_entity, 'res': tmp})
print("预测的结果列表:{}".format(str(res_list)))
