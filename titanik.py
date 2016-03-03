# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 20:56:19 2016

@author: Avalok
"""

from pandas import read_csv, DataFrame, Series
data = read_csv('titanik.csv',delimiter=";")

print(data["Name"])

data.pivot_table('PassengerId', 'Pclass', 'Survived', 'count').plot(kind='bar', stacked=True)

#(fig, axes) = plt.subplots(ncols=2)
data.pivot_table('PassengerId', 'SibSp', 'Survived', 'count').plot(kind='bar', stacked=True)

#считаем сколько
COUNT = data.PassengerId.value_counts()
print("COUNT =", COUNT)

MEDIAN = data["Age"].median()
print("===MEDIAN===")
print(MEDIAN)