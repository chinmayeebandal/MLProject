
"""
Created on Wed Jul 18 14:32:10 2018

Machine learning project which predicts the cost of stock prices 1 day in advance by applying
Linear Regression on current financial data

@author: cbandal
"""

import quandl, math
quandl.ApiConfig.api_key = "Enter_your_APIKey"

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as datetime

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

import numpy as np


style.use('ggplot')

ticker = input("Enter ticker symbol: ")
symbol = 'WIKI/'+ticker;

#using quandl
data = quandl.Dataset(symbol).data()
df = data.to_pandas()
df.to_csv('~/Documents/SummerProjects/MLProject/'+ticker+'.csv')

def load_stock_data():
    return pd.read_csv('~/Documents/SummerProjects/MLProject/'+ticker+'.csv', header=0, index_col='Date', parse_dates=True)

#filter out columns
df = load_stock_data()
df = df.filter(items=['Date', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume'])


print(df.tail()) #print 5 recent closing costs

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0
df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

df.fillna(value=-99999, inplace=True)
forecast_out = int(math.ceil(0.01 * len(df)))

df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

#scale the data
X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)

#forecast of the closing price
close_forecast = X[-forecast_out:]
X = X[:-forecast_out]

df.dropna(inplace=True)

y = np.array(df['Prediction'])

#generate test and training data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)

linR = LinearRegression(n_jobs=-1)

#train data
linR.fit(X_train, y_train)

#test data
testing = linR.score(X_test,y_test)
print("testing: ", testing)

#predict 30 days into future
prediction = linR.predict(close_forecast)
print(prediction)
df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in prediction:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += 86400
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)]+[i]


df['Adj. Close'].plot(figsize=[10,9])
df['Forecast'].plot(figsize=[10,9])

plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()
