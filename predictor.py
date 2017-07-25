from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
from sklearn import svm, tree


# data = pd.read_csv('cleaned data/clean_loan.csv')
data = open('cleaned data/clean_loan.csv').readlines()
train_data = open('cleaned data/train.txt').readline()

X = []
for i in data:
    x = i[:-2].split(',')
    for j in range(len(x)):
        try:
            x[j] = float(x[j])
        except ValueError:
            x[j] = 0
    X.append(x)

Y = [int(x) for x in train_data]

#
test = [
    [49464, 65656, 0, 9, 0, 44512, 54018, 0, 0, 3, 7420, 871.11, 22.8, 3, 0, 0]
]

# SVM
classifier = svm.SVC()
classifier.fit(X, Y)
classifier.predict(test)

# gaussian Naive bayes classifier
nbCls = GaussianNB()
nbCls.fit(X, Y)
nbCls.predict(test)


# dicision tree
dtCls = tree.DecisionTreeClassifier()
dtCls.fit(X, Y)
dtCls.predict(test)
