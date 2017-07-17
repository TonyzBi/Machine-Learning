# -*- coding: utf-8 -*-

from __future__ import print_function, division
import tensorflow as tf
import numpy as np
import load_data


class Network(object):
    """

    """
    def __init__(self, num_hidden, batch_size):
        """

        :param num_hidden: Number of neural network nodes in hidden layer
        :param batch_size: Size of processing data one times
        :return:
        """
        self.num_hidden = num_hidden
        self.batch_size = batch_size

        # Graph Related
        self.graph = tf.Graph()
        self.tf_train_samples = None
        self.tf_train_labels = None
        self.tf_test_samples = None
        self.tf_test_labels = None
        self.tf_test_prediction  = None

    def define_graph(self):
        with self.graph.as_default():
            tf_train

    def train(self):
        pass

    def test(self):
        pass

    def accuracy(self):
        pass
