# -*- coding: utf-8 -*-
"""
@author: Prajwal Bharadwaj N
"""
from sklearn import datasets
iris = datasets.load_iris()

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(iris.data,iris.target,train_size=0.8,test_size=0.2,random_state=100)

from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X_train,y_train)
predicted= model.predict(X_test) 

from sklearn.metrics import classification_report, confusion_matrix
print(confusion_matrix(y_test, predicted))
print(classification_report(y_test, predicted))
