# Code explanation for prediction of CO2 emissions for India with/without carbon pricing

## Analysis.py
To install the required libraries run the following commands.
```
pip3 install pandas
pip3 install numpy
pip3 install matplotlib
```

The dataset for yearwise CO2 emissions of countries from 1990 to 2019 was downloaded from this [link](https://data.worldbank.org/indicator/EN.ATM.CO2E.PC).
The code has been fully commented explaining each line. 

To visualise the plots for different countries, enter the relevant country name in the data.loc field.
I have made a lineplot for visualisation, to get a scatter plot(for discrete values) use plt.scatter(x,y) instead of plt.plot(x,y)

## Percentinc.py
This code gives the percentage increase in CO2 emission from the previous year. The relevant dependencies are already installed from analysis.py . 
To visualise the plots for different countries, enter the relevant country name in the data.loc field.

For some countries the growth rate reaches a negative value. To prevent clipping of the plot, I print the minimum value in the list and accordingly adjust the plt.ylim().

## arima_model.py
ARIMA stands for AutoRegressive Integrated Moving Average. It is a statistical tool which is used for time series data for analysing and prediction of future trends. To apply ARIMA effectively the dataset needs to be made stationary by differencing the data.

It is included in statsmodel for python. To install this run

`pip3 install statsmodels`

ARIMA has 3 parameters : p,d,q
 - p : the number of lag observations in the model, also known as the lag order.
 - d : the number of times the raw observations are differenced to make ; also known as the degree of differencing.
 - q : the size of the moving average window, also known as the order of the moving average.
We import the model. We are trying to predict the future trends for China and India and knowing that China has implemented Carbon Pricing while India has not, we expect China to perform better.

As the absolute values for China are much larger owing to the country size, we need to normalise the values. For the purpose of normalisation, I have used population values from 1990 to 2019 for both India and China and saved them in CSV files(uploaded in the main branch). Any other relevant normalising factor can also be used, for example area of the country.

We divide the values. To apply ARIMA model we need p value below 0.05, initially the dataset gives p value as 0.94, as it is not differenced. On differencing twice we get an optimal value of p and so d value is 2 (this step has not been shown in the final code as we are concerned with this step only to get d value).
We run the model for both the countries, plot and compare the predictions.
