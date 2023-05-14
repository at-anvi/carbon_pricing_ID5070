import numpy as np
import pandas as pd
import os
import math
from matplotlib import pyplot as plt

data=pd.read_csv("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5358347.csv",on_bad_lines='skip')
print("Indicator code is EN.ATM.CO2E.KT")

print("This refers to CO2 emissions in kilo-tonnes unit")
# print(data)

labels =["1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]
df=data.loc[data["Country Name"]=="China"]
arr=np.array(df)
# print(arr)
lst =[]
#We store the percentage increases in a list.
for i in range (5,arr.size):
    lst.append(round((arr[0][i]-arr[0][i-1])*100/arr[0][i-1],2))
#We print the minimum value in the list as it might be negative and corresponding to that we change plt.ylim
print(min(lst))
plt.plot(labels,lst)
plt.ylim(-10, 100)
plt.title("Yearly percentage increase in CO2 Emissions in China")
plt.xlabel("Year")
plt.ylabel("Percentage increase of CO2 Emissions")
plt.show()
