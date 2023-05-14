import numpy as np
import pandas as pd
import os
import math
from matplotlib import pyplot as plt

#We first read the csv file containing information about the CO2 emissions of all countries from 1990 to 2019
data=pd.read_csv("API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5358347.csv",on_bad_lines='skip')

#Indicator code is EN.ATM.CO2E.KT which signifies that we are referring to CO2 emissions in kilo-tonne units
print("This refers to CO2 emissions in kilo-tonnes unit")

#We create a list for each of the years
labels =["1990","1991","1992","1993","1994","1995","1996","1997","1998","1999","2000","2001","2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014","2015","2016","2017","2018","2019"]

#Selecting the particular country for which we want yearwise data
#For different countries change the Country Name
df=data.loc[data["Country Name"]=="Bangladesh"]

#Creating a numpy array with the list
arr=np.array(df)
# print(arr)

#Creating an array with relevant datapoints from the API_EN_ATM
lst =[]
for i in range (4,arr.size):
    lst.append(arr[0][i])
   
#Plotting and visualising the trend
plt.plot(labels,lst)
plt.title("Country")
plt.xlabel("Year")
plt.ylabel("CO2 emissions in kT")
plt.show()
# plt.line(labels, fig)
# plt.show()
