#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 14:32:10 2018

Machine learning project which predicts the cost of stock prices 30 days in advance by applying
Linear Regression on current financial data

@author: cbandal
"""

import quandl
quandl.ApiConfig.api_key = "Enter_your_API_key"

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn import preprocessing, cross_validation

import numpy as np
#import tensorflow as tf


ticker = input("Enter ticker symbol: ")
symbol = 'WIKI/'+ticker;

#using quandl
data = quandl.Dataset(symbol).data()
df = data.to_pandas()
df.to_csv('~/Documents/SummerProjects/MLProject/'+ticker+'.csv')

def load_stock_data():
    return pd.read_csv('~/Documents/SummerProjects/MLProject/AAPL.csv')
    
#filter out Adj close
df = df[['Adj. Close']]
print(df.tail()) #print 5 recent closing costs

forecast_out = int(30)
df['Prediction'] = df[['Adj. Close']].shift(-forecast_out)

#scale the data
X = np.array(df.drop(['Prediction'], 1))
X = preprocessing.scale(X)

#forecast of the closing price
close_forecast = X[-forecast_out:]
X = X[:-forecast_out]

y = np.array(df['Prediction'])
y = y[:-forecast_out]

#generate test and training data
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

linR = LinearRegression()

#train data
linR.fit(X_train, y_train)

#test data
testing = linR.score(X_test,y_test)
print("testing: ", testing)

#predict 30 days into future
prediction = linR.predict(close_forecast)
print(prediction)

#plot the graph
plt.ylabel("Cost")
plt.xlabel("No of days from today")
plt.plot(prediction)
plt.show()
