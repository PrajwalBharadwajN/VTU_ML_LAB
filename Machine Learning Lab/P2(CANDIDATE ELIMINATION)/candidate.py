# -*- coding: utf-8 -*-
"""
@author: Prajwal Bharadwaj N
"""
'''
import csv
a=[]
with open('enjoysport.csv')as trainData:
    for row in csv.reader(trainData):
        a.append(row)
        print(row)
'''

import pandas as pd
df = pd.read_csv('enjoysport.csv',header=None)
a = df.values.tolist()
print(df)
n=len(a[0])-1

print("\n The initial value of hypothesis: ")
s = ['0'] * n
g = ['?'] * n
print ("\n The most specific hypothesis S0 :",s)
print (" \n The most general hypothesis G0 :",g)

s=a[0][:-1]
temp=[]
print("\n Candidate Elimination algorithm\n")

for i in range(len(a)):
    if a[i][n]=="yes": #Use Positive for manufacture.csv
        for j in range(n):
            if a[i][j]!=s[j]:
                s[j]='?'
        for j in range(n):
            for k in range(len(temp)):  #Use len(temp)-1 for manufacture.csv
                if temp[k][j]!='?' and temp[k][j]!=s[j]:
                    del temp[k] 
        
    if a[i][n]=="no": #Use Negative for manufacture.csv
        for j in range(n):
             if s[j]!=a[i][j] and s[j]!='?': 
                 g[j]=s[j]
                 if g not in temp:
                  temp.append(g) 
                 g= ['?']*n

    print("\n For Training Example No :{0} the hypothesis is S{0} ".format(i+1),s)
    if (len(temp)==0):
            print(" For Training Example No :{0} the hypothesis is G{0} ".format(i+1),g)
    else:
            print(" For Training Example No :{0} the hypothesis is G{0}".format(i+1),temp)
