'''
@Time : 2023-10-07 15:33
@Author : laolao
@FileName: data_preprocessing.py
'''
import pickle
import model_dataSource

data = model_dataSource.Data_processing(good_file='data/goodqueries.txt', bad_file='data/nsfocus_isop.txt')
X_train, X_test, y_train, y_test = data.return_train_data()

with open('file/logs.pkl', 'rb') as input:
    v, w = pickle.load(input)
v.fit_transform(data.queries)
w.fit(X_train, y_train)
print('模型的准确度:{}'.format(w.score(X_test, y_test)))

# 保存分类模型和特征提取器
with open('file/logs_add_isop.pkl', 'wb') as f:
    pickle.dump((v, w), f)
