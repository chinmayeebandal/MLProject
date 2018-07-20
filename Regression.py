#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 22:44:53 2018

@author: cbandal
"""
import quandl
quandl.ApiConfig.api_key = "Bx3yLKptEvfyr4cx-VZF"
from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
#from sklearn.model_selection import train_test_split




ticker = input("Enter ticker symbols: ").split(' ')
print(ticker)



for tick in ticker:
    symbol1 = 'WIKI/'+tick+'.0' #date column
    symbol2 = 'WIKI/'+tick+'.4' #closing price column
    start = "2001-12-31"
    end = "2006-12-31"

    data = quandl.get([symbol1, symbol2], start_date=start, end_date=end, returns="numpy")

    #x_pts = np.array([1,2,3,4,5], dtype=np.float64)
    #y_pts = np.array([5,4,6,5,6], dtype=np.float64)

    dates = np.array([x[0] for x in data], dtype=object)
    #print(dates)

    x_pts = np.array([i for i in range(1, dates.size+1)], dtype=np.float64)
    y_pts = np.array([x[1] for x in data], dtype=np.float64)

    #print(x_pts)
    #print(y_pts)

    #x_train,x_test, y_train, y_test = train_test_split(x_pts, y_pts, test_size=0.4)


    def slope_and_yintercept(x_pts, y_pts):
        m = ((mean(x_pts)*mean(y_pts)) - mean(x_pts*y_pts)) / ((mean(x_pts)**2) - (mean(x_pts*x_pts)))
        b = mean(y_pts) - (m * mean(x_pts))
        return m, b

    def squared_error(y_orig, y_line):
        return sum((y_line - y_orig)*(y_line - y_orig))

    def coefficient_of_determination(y_orig, y_line):
        y_mean = [mean(y_orig) for y in y_orig] # ybar
        seRegr = squared_error(y_orig, y_line)
        seYbar = squared_error(y_orig, y_mean)
        return (1-(seRegr/seYbar))
    

    m,b = slope_and_yintercept(x_pts, y_pts)
    regr_line = [(m*x) + b for x in x_pts]

    r_squared = coefficient_of_determination(y_pts, regr_line)
    print(tick," r square: ",r_squared)


    predict_x = 1100
    predict_y = (m*predict_x) + b
    #predict_y = [(m*x) + b for x in x_test]
    print(tick, "predicted cost: ",predict_y)

    plt.title(tick)
    plt.plot(x_pts,y_pts,color='#003F72',label='data')
    plt.plot(x_pts, regr_line, label='regression line')
    plt.plot(predict_x, predict_y, "go", label='prediction')
    plt.xlabel('No of days since start date')
    plt.ylabel('Price')
    plt.legend(loc=4)
    plt.show()

