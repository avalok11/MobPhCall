# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
import numpy

data = pandas.read_csv('January.csv', low_memory=False)

print ("LENGHT=", len(data))
#print ("COLUMNS=", data)

print("")

c1 = data["Номер Владельца"].value_counts(sort=False)
print (c1)
p1 = data['Номер Владельца'].value_counts(sort=False, normalize=True)
print (p1)

