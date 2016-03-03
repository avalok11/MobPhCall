# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
import numpy

#import data from CSV file
data = pandas.read_csv('January.csv', low_memory=False)

#upper-case all DataFrame column names
#data.columns = map(str.upper,data.columns)

#bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

print ("LENGHT=", len(data))            #numbers of observations (rows)
print ("COLUMNS=", len(data.columns)) #number of Variables (columns)

#clean data, we need only phone calls
phone_data = data[(data["Call Direction/Internet,Value Of Service"]!="INTERNET")]
c2 = data["ВИД УСЛУГИ"].value_counts(sort=False)
print (c2)
p2 = data['ВИД УСЛУГИ'].value_counts(sort=False, normalize=True)
print (p2)

ct1 = data.groupby('МЕСТО ВЫЗОВА').size()
print(ct1)

sub1=data[(data['ВИД УСЛУГИ']=='Исходящие') | (data['ВИД УСЛУГИ']=='Исходящие местныевызовы') | (data['ВИД УСЛУГИ']=='Исходящая связь')| (data['ВИД УСЛУГИ']=='Исходящиемеждугородные вызовы')]
sub2=sub1.copy()

print("")
print('counts of Вид Услуги')
c3 = sub2['НОМЕР ВЛАДЕЛЬЦА'].value_counts(sort=False)
#print(c3)
for c,cc in c3.items():
    print (c,cc)



print("")