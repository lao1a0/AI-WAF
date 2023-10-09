'''
@Time : 2023-10-09 15:37
@Author : laolao
@FileName: mode_dataSource.py
'''
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import urllib


class Data_processing:

    def __init__(self, good_file='data/goodqueries.txt', bad_file='data/badqueries.txt'):
        ''':cvar
        对输入的文本进行打标签，0是正常的流量，1是恶意的流量
        '''
        good_query_list = self.get_query_list(good_file)
        good_y = [0 for i in range(0, len(good_query_list))]
        bad_query_list = self.get_query_list(bad_file)
        bad_y = [1 for i in range(0, len(bad_query_list))]
        self.vectorizer = TfidfVectorizer(tokenizer=self.get_ngrams)
        self.queries = bad_query_list + good_query_list
        self.X = self.vectorizer.fit_transform(self.queries)
        self.y = bad_y + good_y

    def return_train_data(self):
        return train_test_split(self.X, self.y, test_size=0.2, random_state=42)

    def get_query_list(self, filename):
        directory = str(os.getcwd())
        filepath = directory + "/" + filename
        data = open(filepath, 'r', encoding='utf8').readlines()
        query_list = []
        for d in data:
            d = str(urllib.parse.unquote(d))
            query_list.append(d)
        return list(set(query_list))

    def get_ngrams(self, query):
        tempQuery = str(query)
        ngrams = []
        for i in range(0, len(tempQuery) - 3):
            ngrams.append(tempQuery[i:i + 3])
        return ngrams


if __name__ == '__main__':
    data = Data_processing()
    print(data.return_train_data())
