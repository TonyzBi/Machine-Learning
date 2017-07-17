# -*- coding: utf-8 -*-

from scipy.io import loadmat as load
import numpy as np

class Datasets(object):
    @staticmethod
    def getdata():
        train_data = load('./data/train_32x32.mat')
        test_data  = load('./data/test_32x32.mat')
        return train_data,test_data

if __name__ == '__main__':
    train, test = Datasets.getdata()
    print train['X'].shape
    print train['y'].shape
    print train['y'][:5,:]



