'''
@Time : 2023-10-09 14:10
@Author : laolao
@FileName: model_training.py
'''
import pickle
import model_dataSource
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

data = model_dataSource.Data_processing()
X_train, X_test, y_train, y_test = data.return_train_data()

lr = LogisticRegression(penalty='l2', C=1.0, solver='liblinear')
acc=[]
for i in range(50):
    history = lr.fit(X_train, y_train)
    acc.append(history.score(X_test, y_test))
    # print('The accuracy of LogisticRegression is:', acc)

with open('file/logs.pkl', 'wb') as f:
    pickle.dump((data.vectorizer, lr), f)

# 绘制每一轮acc的折线图
plt.plot(range(1, len(acc)+1), acc, 'bo', label='Test acc')
plt.title('Test Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.show()