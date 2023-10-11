#!python
# -*- coding: utf-8 -*-
# @author: Kun

'''
Author: Kun
Date: 2022-05-05 14:57:22
LastEditTime: 2022-12-11 16:11:03
LastEditors: Kun
Description: 
FilePath: /AI-WAF/models/text_cnn_1.py
'''

from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Embedding, Input, SpatialDropout1D
from tensorflow.keras.layers import Conv1D, Flatten, Dropout, MaxPool1D, concatenate
from tensorflow.keras.regularizers import l2

class_num = 2
inputLen = 1024

def textcnn1(tokenizer, class_num=2):
    kernel_size = [1, 3, 5]
    acti = 'relu'
    my_input = Input(shape=(inputLen,), dtype='int32')
    emb = Embedding(len(tokenizer.word_index) + 1, 20, input_length=inputLen)(my_input)
    emb = SpatialDropout1D(0.2)(emb)

    net = []
    for kernel in kernel_size:
        con = Conv1D(32, kernel, activation=acti, padding="same", kernel_regularizer=l2(0.0005))(emb)
        con = MaxPool1D(2)(con)
        net.append(con)
    net = concatenate(net, axis=-1)
    net = Flatten()(net)
    net = Dropout(0.5)(net)
    net = Dense(256, activation='relu')(net)
    net = Dropout(0.5)(net)
    net = Dense(class_num, activation='softmax', kernel_regularizer=l2(l=0.001))(net)
    model = Model(inputs=my_input, outputs=net)
    return model
