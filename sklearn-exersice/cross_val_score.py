# -*- coding: utf-8 -*-

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.cross_validation import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt


data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=4)

# print float(len(X_train))/len(X_test)
# print len(X_test)
def fun1():

    knn = KNeighborsClassifier()
    knn.fit(X_train, y_train)

    print knn.score(X_test, y_test)


def fun2():
    k_range = range(1, 31)
    k_scores = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, X, y, cv=5, scoring='accuracy')
        k_scores.append(scores.mean())

    plt.plot(k_range, k_scores)
    plt.xlabel('Value of K for KNN')
    plt.ylabel('Cross-Validated Accuracy')
    plt.show()

def fun3():
    k_range = range(1, 31)
    k_scores = []
    for k in k_range:
        knn = KNeighborsClassifier(n_neighbors=k)
        scores = -cross_val_score(knn, X, y, cv = 10, scoring='mean_squared_error')
        k_scores.append(scores.mean())
    plt.plot(k_range, k_scores)
    plt.xlabel('Value of K for KNN')
    plt.ylabel('Mean_squared_error')
    plt.show()



def fuction(**options):
    """

    :param a: is the first para
    :param b: is the second par
    :return:
    """
    a = options.pop('a', None)
    b = options.pop('b', None)
    if a and b:

        print a,b

if __name__ == '__main__':
    fun3()

