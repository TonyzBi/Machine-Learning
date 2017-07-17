# -*- coding: utf-8 -*-

import numpy as np

def kmeans(X, k, maxIt):
    numPoints, numDim = X.shape

    dataSet = np.zeros((numPoints, numDim + 1))
    dataSet[:, :-1] = X

    # initialize center points ramdomly
    #centroids = dataSet[np.random.randint(numPoints, size=k), :] 容易选取重复点，出错
    centroids = dataSet[:k, :]
    #centroids = dataSet[0:2, :]
    # Ramdomly assign labels to initial center points
    centroids[:, -1] = range(1, k + 1)

    # Initialize book keeping vars
    iterations = 0
    oldCentroids = None

    # Run the main k-means algoriths
    while not shouldStop(oldCentroids, centroids, iterations, maxIt):

        print 'Iteration: ', iterations
        print 'Dataset: ', dataSet
        print 'centroids: ', centroids

        oldCentroids = np.copy(centroids)
        iterations += 1

        updateLabels(dataSet, centroids)

        centroids = getCentroid(dataSet, k)

    return dataSet

def shouldStop(oldCentroids, centroids, iterations, maxIt):
    if iterations > maxIt:
        return True
    return np.array_equal(oldCentroids,centroids)

def updateLabels(dataSet, centroids):
    numPoints, numDim = dataSet.shape
    for i in range(0, numPoints):
        dataSet[i, -1] = getLabelFromCloseCentroid(dataSet[i, :-1], centroids)


def getLabelFromCloseCentroid(dataSetRow, centroids):
    label = centroids[0, -1]
    minDist = np.linalg.norm(dataSetRow - centroids[0, :-1])
    for i in range(1, centroids.shape[0]):
        dist = np.linalg.norm(dataSetRow - centroids[i, :-1])
        if dist < minDist:
            minDist = dist
            label = centroids[i, -1]

    return label

def getCentroid(dataSet, k):
    """

    :param dataSet:
    :param k:
    :return: new center points
    """
    result = np.zeros((k, dataSet.shape[1]))  # k rows dataset columes
    for i in range(1, k + 1):
        oneCluster = dataSet[dataSet[:, -1] == i, :-1]
        result[i -1, :-1] = np.mean(oneCluster, axis= 0 ) # 对列求均值
        result[i -1, -1] = i

    return result


def main():
    x1 = np.array([1, 1])
    x2 = np.array([2, 1])
    x3 = np.array([4, 3])
    x4 = np.array([5, 4])
    testX = np.vstack((x1, x2, x3, x4))

    result = kmeans(testX, 2, 10)

    print 'K-means: \n', result

if __name__ == '__main__':
    main()









