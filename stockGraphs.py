#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 00:47:21 2018

@author: cbandal
"""

import quandl, math
quandl.ApiConfig.api_key = "API"
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import datetime as datetime


def printGraph(ticker, start_date, end_date):

    #symbol1 = 'WIKI/'+tick+'.0' #date column
    #symbol2 = 'WIKI/'+tick+'.1' #opening price column
    # symbol3 = 'WIKI/'+tick+'.4' #closing price column
    symbol = "WIKI/"+ticker    
    data = quandl.get(symbol, start_date=start_date, end_date=end_date)
    data = data.filter(items=['Date', 'Open', 'High', 'Low', 'Close', 'Volume'])
    
    print(data.tail(10))
    plt.title(ticker)
    plt.plot(data['Close'])
    plt.xlabel("Period")
    plt.ylabel("CLosing price")
    plt.show()
        
printGraph("AAPL", "2018-01-01", "2018-05-31")

#add percent change later    
def stockPrediction(ticker, start_date, end_date):
    symbol = "WIKI/"+ticker    
    data = quandl.get(symbol, start_date=start_date, end_date=end_date)
    data = data.filter(items=['Date', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume'])
    
    data['HL_Percent'] = (data['Adj. High']-data['Adj. Low']) / data['Adj. Close']
    data['Return_Percent'] = (data['Adj. Close']-data['Adj. Open']) / data['Adj. Close']
    
    #prepare data
    data = data[['Adj. Close', 'HL_Percent', 'Return_Percent', 'Adj. Volume']]
    data.fillna(value=-99999, inplace=True)
    
    forecast_out = int(math.ceil(0.01 * len(data)))
    forecast_col = 'Adj. Close'
    #forecast_out = 5
    data['Prediction'] = data[[forecast_col]].shift(-forecast_out)
    #print(data)
    
    #scale data
    X = np.array(data.drop(['Prediction'], 1))
    X = preprocessing.scale(X)
    X = X[:-forecast_out]
    closing_forecast = X[-forecast_out:] #gotta predict values in this
    
    data.dropna(inplace=True)
    y = np.array(data['Prediction'])
    
    #generate training and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    #linear regression
    linR = LinearRegression(n_jobs=-1) #use as much threads as possible
    
    #fit and train data
    linR.fit(X_train, y_train)
    
    r_sq = linR.score(X_test, y_test)
    print("Coefficient of difference: ", r_sq)
    
    prediction = linR.predict(closing_forecast)
    data['Forecast'] = np.nan #populate later
    
    last_date = data.iloc[-1].name
    last_day = last_date.timestamp()
    one_day_secs = 86400
    next_day = last_day+one_day_secs
    
    print("Prediction of Closing price: ")
    for i in prediction:
        next_date = datetime.datetime.fromtimestamp(next_day)
        next_day += 86400
        print(datetime.datetime.fromtimestamp(next_day), i) #print the future prices after last date
        data.loc[next_date] = [np.nan for _ in range(len(data.columns)-1)]+[i]
    
def getClosingPrice(ticker, start_date, end_date):
    symbol = "WIKI/"+ticker    
    data = quandl.get(symbol, start_date=start_date, end_date=end_date)
    data = data.filter(items=['Date', 'Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume'])

    close = data.iloc[-1][3]
    return close
    
#stockPrediction("AAPL", "2018-01-01", "2018-05-31")
#blah = getClosingPrice("AAPL", "2018-01-01", "2018-05-31")

         
        
        
        
    
