# -*- coding: utf-8 -*-

from __future__ import print_function
import matplotlib.pyplot as plt
import numpy as np
import load_data

num_labels = 10
image_size = 32

def reformat(samples, labels):
    """
    改变图片数据的形状 图片高 通道数
    将 2 转化为 [0,0,1, 0,0,0,00000]
    :param samples:
    :param labels:
    :return:
    """
    # labels = np.array([x[0] for x in labels])
    # one_hot_labels = []
    # for num in labels:
    #     one_hot = [0.0] * 10
    #     if num == 10:
    #         one_hot[0] = 1.0
    #     else:
    #         one_hot[num] = 1.0
    #     one_hot_labels.append(one_hot)
    #
    # labels = np.array(one_hot_labels).astype(np.float32)

    newsample=np.transpose(samples,(3,0,1,2))
    newlabels = np.zeros([labels.shape[0], 10])
    for i, lab in enumerate(labels):
        # print('lab: ', lab)
        if lab == 10:
            newlabels[i, 0] = 1.0
        else:
            newlabels[i, lab] = 1.0

    return newsample, newlabels

def normalize(samples):
    """

    :param samples:
    :return:
    """
    single_channel = np.add.reduce(samples, keepdims = True, axis =3)
    single_channel = single_channel / 3.0
    return (single_channel /128.0 - 1.0)
    # return single_channel


def distribution(labels, name):
    """

    :param labels:
    :param name:
    :return:
    """
    pass

def inspect(dataset, labels, i):
    """
    show picture
    :param dataset:
    :param labels:
    :param i:
    :return:
    """
    print(labels[i])
    # print(dataset[i])
    plt.imshow(dataset[i])
    plt.show()

if __name__ == '__main__':
    train, test = load_data.Datasets.getdata()
    train_samples = train['X']
    train_lables = train['y']
    test_samples = test['X']
    test_labels = test['y']

    train_samples, train_lables = reformat(train_samples, train_lables)

    inspect(train_samples, train_lables, 2)
    train_samples = normalize(train_samples)
