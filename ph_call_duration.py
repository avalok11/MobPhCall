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

#clean data, we need only phone calls, reject INTERNET from "Call Direction.." raw
#phone_data = data[(data["Call Direction/Internet"]!="INTERNET") & (data["Call Direction/Internet"]!="ANYAPN") & (data["Call Direction/Internet"]!="ptcp=000010000") & (data["Call Direction/Internet"]!="ptcp=000010009") & (data["Call Direction/Internet"]!="MMS") & (data["Kind Of Service"]!="Входящие СМС") & (data["Kind Of Service"]!="СМС исходящие") & (data["Kind Of Service"]!="ММС входящие") & (data["Kind Of Service"]!="ММС исходящие")]
phone_data = data[(data["Measurement"]=="Минута") | (data["Measurement"]=="Секунда")]
phone_data = phone_data[(phone_data["Kind Of Service"]!="Дополнительные услуги")]

#agregation ph data to pivot table - to have data
ph_data_pivot = phone_data.pivot_table(values=["Call Direction/Internet"],index=["Phone Owner"], columns=["Kind Of Service"], aggfunc="count") #.plot(kind='bar', stacked=True)
# add to pivot table RAW = summ of all calls
#ph_data_pivot['Call Direction/Internet']['summ'] = ph_data_pivot['Call Direction/Internet']['Income Call']+ph_data_pivot['Call Direction/Internet']['Incomming_ Call']

print("PIVOT============")
print(ph_data_pivot['Call Direction/Internet']['Income Call'])
print("PIVOT============")

for k,v in ph_data_pivot:
    print ("KEY - ",k)
    print ("VALUE - ",ph_data_pivot[k][v])

#now we are counting total amount of phone call (income and outcome), count by "Phone Owner' raw
call_amount = phone_data["Phone Owner"].value_counts(sort=False)
call_amount_percent = phone_data["Phone Owner"].value_counts(sort=False, normalize=True)*100

#display Series  - amunt of calls
print("Phone Owner    Number Of Calls")
print(call_amount)

#display Series amount of calls by percentage
print("Phone Iwner    Percentage of Calls")
print(call_amount_percent)

#call_amount_percent.plot(kind='bar')
#call_amount.plot(kind='pie')
