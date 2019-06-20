"""
    Apply 2-2-1 perceptron to iris dataset from scratch
    Author: FrankYe
"""

import numpy as np
import math
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler

'''
    从sklearn导入鸢尾花数据集，由于2-2-1网络结构，
    取鸢尾花数据集的前两列属性，以及前100条数据
'''
iris = datasets.load_iris()
X = iris.data[:100, :2]
y = iris.target[:100]

# 标准化初始数据
X = MinMaxScaler().fit_transform(X)

# 设定网络权重
w1 = np.array([[1.0, 1.0], [1.0, 1.0]])
w2 = np.array([[1.0], [1.0]])


def sigmoid(x):
    y = 1.0 / (1.0 + math.exp(-x))
    return y


def first_layer(x):
    y = x
    return y


def activate(x, threshold, type='normal'):
    """
        x is a matrix, threshold is equal to bias
    """
    tmp = x + threshold
    if type == 'normal':
        res = np.vectorize(lambda x: 1 if x > 0 else 0)(tmp)
        return res
    elif type == 'sigmoid':
        res = np.vectorize(sigmoid)(tmp)
        return res
    else:
        raise RuntimeError


def normal_layer(x, w, threshold):
    value = x.dot(w)
    res = activate(value, threshold, type='sigmoid')
    return res


def get_loss(yhat, y):
    return 0.5 * (yhat - y) ** 2


def sigmoid_deriv(x):
    return sigmoid(x) * (1 - sigmoid(x))


def update_weight(loss, x, w1, w2, ly2_out, learning_rate=0.01):
    # update weight2
    loss_yhat_deriv = loss
    zp = ly2_out.dot(w2)
    yhat_sigmoid_deriv = sigmoid_deriv(zp)
    sigmoid_w2_deriv = ly2_out
    w2_new = w2 - learning_rate * loss_yhat_deriv * yhat_sigmoid_deriv * np.transpose(sigmoid_w2_deriv)
    # update weight1
    for col in range(w1.shape[0]):
        w1[:, [col]] -= learning_rate * loss_yhat_deriv * yhat_sigmoid_deriv * w2[col] * sigmoid_deriv(x.dot(w1[:, [col]])) * x[col]
    return w2_new, w1


if __name__ == '__main__':
    n_epoch = 200
    for epoch in range(n_epoch):
        print('=================================')
        print('epoch is {}'.format(epoch + 1))
        total_loss = 0
        print('total loss start is', total_loss)
        for i in range(X.shape[0]):
            ly1_out = first_layer(X[i, :])
            ly2_out = normal_layer(ly1_out, w1, np.array([[-0.5, 1.5]]))
            ly3_out = normal_layer(ly2_out, w2, np.array(-1.5))
            loss = get_loss(ly3_out, y[i])
            total_loss += loss
            w2_new, w1_new = update_weight(loss, ly1_out, w1, w2, ly2_out, learning_rate=0.0001)
            w2, w1 = w2_new, w1_new
        w2, w1 = w2_new, w1_new
        print('total loss is {}'.format(total_loss))
    train_w1, train_w2 = w1, w2

    # 200轮训练后的权重
    print('weight1 of model is', w1)
    print('weight2 of model is', w2)
