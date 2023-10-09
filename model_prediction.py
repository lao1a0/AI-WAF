'''
@Time : 2023-10-09 16:42
@Author : laolao
@FileName: model_prediction.py
'''

import pickle

with open('file/logs_add_isop.pkl', 'rb') as input:
    v, w = pickle.load(input)

with open("data/badqueries.txt", "r", encoding='utf-8') as f:
    my_code = f.readlines()

def predict(my_code,v, w):
    X_predict = v.transform(my_code)
    res = w.predict(X_predict)
    res_list = []

    for q, r in zip(my_code, res):
        tmp = '正常请求' if r == 0 else '恶意请求'
        res_list.append({'url': q, 'res': tmp})

    import pandas as pd

    df = pd.DataFrame(res_list)
    print("恶意请求：")
    print(df.loc[df['res'] == '恶意请求'].count())
    print("正常请求：")
    print(df.loc[df['res'] == '正常请求'].count())
    df.to_csv("output.csv")
    return df
predict(my_code,v, w)
