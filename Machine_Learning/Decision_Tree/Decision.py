#! -*- coding: utf-8 -*-

import csv
from sklearn.feature_extraction import DictVectorizer
from sklearn import preprocessing
from sklearn import tree
from sklearn.externals.six import StringIO

dataset = open(r'./buy_computer.csv')
readers = csv.reader(dataset)

titles = readers.next()
print titles

featureList = []
labelList = []

for line in readers:
    if len(line) == 6:
        labelList.append(line[-1])
        featureList.append(dict(zip(titles[1:-1],line[1:-1])))
    else:
        raise Exception


print labelList
print featureList

vec = DictVectorizer()
inputX = vec.fit_transform(featureList).toarray()

print 'InputX: ' + str(inputX)
print(vec.get_feature_names())

lb = preprocessing.LabelBinarizer()
outputY = lb.fit_transform(labelList)


print 'OutputY: '+ str(outputY)

clf=tree.DecisionTreeClassifier(criterion="entropy") #建立决策树模型 entropy表示用ID3算法，默认是调用GINI算法
clf.fit(inputX,outputY)

print 'Decision Tree: '+ str(clf)

with open("DecisionTree.dot",'w') as fp:
    fp = tree.export_graphviz(clf, feature_names=vec.get_feature_names(), out_file=fp)


oneRowX=inputX[0,:]
print("oneRowX:"+str(oneRowX))

newRowX=oneRowX

newRowX[0] = 1
newRowX[2] = 0

print 'NewRow: ' + str(newRowX)

predictedY = clf.predict(newRowX)

print "predictedY:" + str(predictedY)



dataset.close()