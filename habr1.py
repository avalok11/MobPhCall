# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas
import numpy

data = pandas.read_csv('January.csv', low_memory=False)

#upper-case all DataFrame column names
#data.columns = map(str.upper,data.columns)

#bug fix for display formats to avoid run time errors
pandas.set_option('display.float_format', lambda x:'%f'%x)

print ("LENGHT=", len(data))            #numbers of observations (rows)
print ("COLUMNS=", len(data.columns)) #number of Variables (columns)

#use PIVOT
#t1 = data[data['Call Direction/Internet']!="INTERNET"]
#t1 = t1[t1['Call Direction/Internet']!="ptcp=000010000"]

#pivot_data2 = pandas.pivot_table(t1, index=['Kind Of Service','Measurement'], values=['Value Of Service'], aggfunc=numpy.sum).plot(kind='bar')
#pivot_data = pandas.pivot_table(data, index=['НОМЕР ВЛАДЕЛЬЦА','ВИД УСЛУГИ','ЕДИНИЦАТАРИФИКАЦИИ(МИН_ СЕК_ ШТ_KB_ MB)'], values=['ПРОД/ОБЪЕМ'], aggfunc=numpy.sum)
#print(pivot_data)

phone_data = data[(data["Measurement"]=="Минута") | (data["Measurement"]=="Секунда")]
phone_data = phone_data[(phone_data["Kind Of Service"]!="Дополнительные услуги")]

#grp_phone_data=phone_data.groupby('Phone Owner')

#data.pivot_table('PassengerId', 'Pclass', 'Survived', 'count').plot(kind='bar', stacked=True)
phone_data.pivot_table('Time','Phone Owner','Kind Of Service','count').plot(kind='bar', stacked=True, legend=False)

#pd=pandas.pivot_table('Date','Phone Owner','Kind Of Service','count')

phone_data.pivot_table(values=["Call Direction/Internet"],index=["Phone Owner"], columns=["Kind Of Service"], aggfunc="count").plot(kind='bar', stacked=True)

#phone_data.pivot_table(values=["Value Of Service"], index=["Phone Owner"], columns=["Kind Of Service"], aggfunc="sum").plot(kind='bar', stacked=True)





#phone_data.pivot_table()


#print("DATA FROM CSV")
#print(data)

#t1 = data[data['ДАТА']=="01.01.16"]
#print(t1["ДАТА"])


print("")