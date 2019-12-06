# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 16:02:16 2019

@author: Prajwal Bharadwaj N
"""
from functools import reduce
import pprint
import pandas as pd

def calculate_priori():
        class_values = list(set(data[class_attr]))
        for i in class_values:
            priori[i]  = class_data.count(i)/float(len(class_data))
        print ("Priori Values: ", priori)
   
def get_cp(attr, attr_type, class_value):
        data_attr = list(data[attr])
        total = 0
        for i in range(0, len(data_attr)):
            if class_data[i] == class_value and data_attr[i] == attr_type:
                 total+=1
        return total/float(class_data.count(class_value))

def calculate_conditional_probabilities(hypothesis):
    for i in priori:
        cp[i] = {}
        for j in hypothesis:
                cp[i].update({ hypothesis[j]: get_cp(j, hypothesis[j], i)})
    print ("\nCalculated Conditional Probabilities: \n")
    pprint.pprint(cp)

def classify():
        print ("Result: ")
        for i in cp:
            print (i, " ==> ", reduce(lambda x, y: x*y, cp[i].values())*priori[i])

data = pd.read_csv("tennis.csv")
print(data)
class_attr = 'PlayTennis'
print("Class Attribute:", class_attr)
class_data =  list(data[class_attr])
priori,cp={},{}
calculate_priori()
hypothesis = {"Outlook":'Sunny', "Temperature":"Cool", "Humidity":'High' , "Windy":'Strong'}
print(hypothesis)
calculate_conditional_probabilities(hypothesis)
classify()
print("-------------------------------------------------------")
hypothesis = {"Outlook":'Overcast', "Temperature":"Mild", "Humidity":'Normal' , "Windy":'Weak'}
print(hypothesis)
calculate_conditional_probabilities(hypothesis)
classify()
