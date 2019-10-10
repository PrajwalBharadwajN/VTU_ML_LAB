# -*- coding: utf-8 -*-
"""
@author: PRAJWAL BHARADWAJ N
"""

from pprint import pprint
import pandas as pd
df_golf = pd.read_csv("golf.csv")
print(df_golf)
attribute_names = list(df_golf.columns)
print("List of Attributes:", attribute_names)
attribute_names.remove('label')
print("Predicting Attributes:", attribute_names)
table=dict()
priorProb=dict()
train=df_golf.sample(frac=0.6,random_state=100) #random state is a seed value
test=df_golf.drop(train.index)
print("---------------------------------")
print(train)
print("---------------------------------")
print(test)
print("---------------------------------")
for attr_val, data_subset in train.groupby("label"):
    from collections import Counter
    valueCount = dict()
    count=0
    for attr_value in attribute_names:
        cnt = Counter(x for x in data_subset[attr_value])
        count=sum(cnt.values())
        valueCount[attr_value]=dict(cnt)
        print("value count", valueCount.values())
        print("counter:-",cnt)
    table[attr_val]=valueCount
    priorProb[attr_val]=count
print("*******************************************")
print("\n\nThe Resultant table is :\n")
pprint(table)
pprint(priorProb)
totalSize=test['label'].count()
correctPridictions=0
for k, row in test.iterrows():
    rowTuple=dict(row)
    print("print row tuple")
    pprint(rowTuple)
    postioriList=list()
    labelList=list()
    for label in table.keys():
        posteriori = 1.0
        print("RowTuple",rowTuple.keys())
        print("RowValues",rowTuple.values())
        for key in [x for x in rowTuple.keys() if x != 'label']:
            print(key, "label:",label)
            attributeValue=rowTuple.get(key)
            if attributeValue in table[label][key].keys():
                countList=table[label][key].values()
                attributeCount=table[label][key][attributeValue]
                posteriori=1.0*attributeCount/sum(countList)*posteriori
        posteriori=posteriori*priorProb[label]
        labelList.append(label)
        postioriList.append(posteriori)
        print(labelList)
        print(postioriList)
    maxProbInd = postioriList.index(max(postioriList))
    print(rowTuple['label'], "::::", labelList[maxProbInd])
    if rowTuple['label'] == labelList[maxProbInd]:
        print(rowTuple['label'],"::::",labelList[maxProbInd])
        correctPridictions=correctPridictions+1
        print("POSTERIORI OF:",label,"is:",posteriori)
print("Number of Correct Predictions : Number of Samples",correctPridictions,":",totalSize)
print("Accuracy:",100.0*correctPridictions/totalSize)