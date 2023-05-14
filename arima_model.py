import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

#importing the ARIMA model and adfuller for parameter estimation
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.stattools import adfuller

#reading China's and India's emission values
df=pd.read_csv("China_emis.csv")
df1=pd.read_csv("India_emis.csv")

#reading India and China population values from 1990 to 2019
popind=pd.read_csv("India_pop.csv")
popchin=pd.read_csv("Chin_pop.csv")

#Normalising emission values with respect to population
for i in range (0,30):
    df['Emission in kT'][i]=df['Emission in kT'][i]/popchin['Population'][i]
for i in range (0,30):
    df1['Emission in kT'][i]=df1['Emission in kT'][i]/popind['Population'][i]    
    
#Indexing according to year
df.set_index('Year',inplace=True)
df1.set_index('Year',inplace=True)

#Finding the p value. The p value must fall below 0.05. We find that applying df.diff.dropna() twice.
#gives a p value close to zero. This means that d value is 2 and we choose q value as 2 from the set {0,1,2} for best performance
result = adfuller(df['Emission in kT'])
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('Critical Values:')
for key, value in result[4].items():
    print('\t%s: %.3f' % (key, value))
#Running the model for China
model = ARIMA(df['Emission in kT'], order=(1,2,2))
results = model.fit()
predictions = results.predict(start=0, end=41)
#Running the model for India
model1=ARIMA(df1['Emission in kT'], order=(1,2,2))
results1 =model1.fit()
predictions1=results1.predict(start=0,end=41)
#Plotting the required predictions
plt.plot(predictions1, color='red')
plt.show()
