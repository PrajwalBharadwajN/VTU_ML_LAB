# -*- coding: utf-8 -*-
"""
@author: PRAJWAL BHARADWAJ N
"""
import csv
a=[]
with open('enjoysport.csv')as trainData:
    for row in csv.reader(trainData):
        a.append(row)
        print(row)
n=len(a[0])-1
S=['0']*n
print("Initial hypothesis ",S)
print("FIND S ALGORITHM")
S=a[0][:-1]
for i in range(len(a)):
    if a[i][n]=="yes":
        for j in range(n):
            if a[i][j]!=S[j]:
                S[j]='?'
    print("\nTraining example no {0}, Hypothesis is".format(i+1),S)
print("\nMaximally specific hypothesis is ", S )
        