'''
@Time : 2023-10-09 14:10
@Author : laolao
@FileName: model_training.py
'''
import pickle
import model_dataSource

data = model_dataSource.Data_processing()
X_train, X_test, y_train, y_test = data.return_train_data()


def train(user=1, save_model_name='file/logs.pkl'):
    if user == 1:
        from sklearn.linear_model import LogisticRegression
        model = LogisticRegression(penalty='l2', C=1.0, solver='liblinear', max_iter=50)
        acc = []
        history = model.fit(X_train, y_train)
        acc.append(history.score(X_test, y_test))
        print('The accuracy of LogisticRegression is:', acc)
    elif user == 2:
        import models.text_cnn_1 as textCNN_1
        model = textCNN_1(tokenizer, 2)

    with open(save_model_name, 'wb') as f:
        pickle.dump((data.vectorizer, model), f)


# # 绘制每一轮acc的折线图
# plt.plot(range(1, len(acc)+1), acc, 'bo', label='Test acc')
# plt.title('Test Accuracy')
# plt.xlabel('Epochs')
# plt.ylabel('Accuracy')
# plt.legend()
# plt.show()

if __name__ == '__main__':
    pass
