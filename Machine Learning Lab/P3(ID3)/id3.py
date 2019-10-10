# -*- coding: utf-8 -*-
"""
@author: PRAJWAL BHARADWAJ N
"""

import pandas as pd
from math import log
from pprint import pprint

df = pd.read_csv('tennis.csv')
data = df.values.tolist()
attr_names = df.columns.values.tolist()
print(df)

def entropy(pos, neg):
    if pos == 0 or neg == 0:
        return 0
    tot = pos + neg
    return -pos / tot * log(pos / tot, 2) - neg / tot * log(neg / tot, 2)

def gain(data, attr, pos, neg):
    d, E, acu = {}, entropy(pos, neg), 0
    for i in data:
        if i[attr] not in d:
            d[i[attr]] = {}
        d[i[attr]][i[-1]] = 1 + d[i[attr]].get(i[-1], 0)
    for i in d:
        tot = d[i].get('Yes', 0) + d[i].get('No', 0)
        acu += tot / (pos + neg) * entropy(d[i].get('Yes', 0), d[i].get('No', 0))
    return E - acu


def build(data, attr_names):
    pos, sz = len([x for x in data if x[-1] == 'Yes']), len(data[0]) - 1
    neg = len(data) - pos
    if neg == 0 or pos == 0:
        return 'Yes' if neg == 0 else 'No'

    root = max([[gain(data, i, pos, neg), i] for i in range(sz)])[1]     
    fin, res = {}, {}
    uniq_attr = set([x[root] for x in data])
    for i in uniq_attr:
        res[i] = build([x[:root] + x[root + 1:] for x in data if x[root] == i], attr_names[:root] + attr_names[root+1:])
    fin[attr_names[root]] = res
    return fin

tree = build(data, attr_names)
pprint(tree)