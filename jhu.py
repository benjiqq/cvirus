import pandas as pd
import numpy as np

df = pd.read_csv("time_series_covid19_confirmed_global.csv", sep=',')

#state
#1 country

#df.iloc[50][1]
"""
for i in range(10):
    r = 10 # row number i.e. date
    c = df.iloc[i][1]
    print (i,c,r)
    #j = df.iloc[i][r]
    #if j > 100:
    #    print (i,c,j)
"""

china_rows = df[(df.Country == 'China')]
sum = 0
for r in china_rows.iloc[-10:-1]:
    x = china_rows[r]
    try:
        sum +=x
    except:
        print (x)

print ("?? ",sum)
