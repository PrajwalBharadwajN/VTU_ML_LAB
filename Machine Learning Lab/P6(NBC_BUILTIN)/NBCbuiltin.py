# -*- coding: utf-8 -*-
"""
@author: Prajwal Bharadwaj N
"""
import pandas as pd
df_imdb = pd.read_csv("imdb_labelled.txt",sep='\t',index_col=None)
print(df_imdb.keys())
print(df_imdb)
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df_imdb['Text'], df_imdb['Label'],train_size=0.8,test_size=0.2,random_state=100)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X_train_cv = cv.fit_transform(X_train)
X_test_cv = cv.transform(X_test)

from sklearn.naive_bayes import MultinomialNB
naive_bayes = MultinomialNB()
naive_bayes.fit(X_train_cv, y_train)
predictions = naive_bayes.predict(X_test_cv)

from sklearn.metrics import accuracy_score, precision_score, recall_score
print('Accuracy score: ', accuracy_score(y_test, predictions))
print('Precision score: ', precision_score(y_test, predictions))
print('Recall score: ', recall_score(y_test, predictions))