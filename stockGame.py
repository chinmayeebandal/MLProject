#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 00:01:24 2018

@author: cbandal
"""

#from StockRegre import stock
import stockGraphs as sg
import pandas as pd
import numpy as np
import math

class simulator:
    
    beginAmt = float(10000);
    stocks = {} #dictionary
    
    def __init__(self, name):
        self.name = name
        self.beginAmt = 100000 #each player begins with $100,000 in their account
    
    name = input("Enter your name: ")
    tickers = input("Which stocks are you interested in? ").split(' ')
    date_range = input("Date range YYYY-MM-DD: ").split(' ')
    #see stock market
    for tick in tickers:
        print(tick)
        sg.printGraph(tick, date_range[0], date_range[1]) #gives general info
        
    
    
   # buy_or_sell = input("Do you wanna buy or sell stocks?(Buy or Sell and Stock): ").split(' ')
    #choice = buy_or_sell[0]
    #stockTicker = buy_or_sell[1]
    #num = int(input("How many do you want to "+choice+" ? "))
    
    if(beginAmt == 100000):
        buy = input("Purchase stocks?(yes/no, Enter company code, # of stocks): ").split(' ')
        if(buy == "yes"):
            for tick in buy:
                sg.printGraph(tick, date_range[0], date_range[1]) #gives general info
                close = sg.getClosingPrice(tick, date_range[0], date_range[1])
                total = close * int(buy[2])
                beginAmt -= total
                
                if stocks.get(tick)==None:    
                    stocks[tick] = int(buy[2])
                else:
                    val = stocks.get(tick)
                    val += int(buy[2])
                
                #sg.stockPrediction(tck, date_range[0], date_range[1]) 
        else:
            predict = input("Do you wanna see any predictions for stock prices? **DISCLAIMER: DO NOT make any purchases based on these predictions")
            if(predict=="yes"):
                tck = input("Please enter the ticker symbol: ")
                sg.stockPrediction(tck, date_range[0], date_range[1]) #predicts future stock prices
            else:
                print("Stocks are cool")
    elif beginAmt<100000 and beginAmt>0.0:
        
        

           
        
    
    
    
    
    
        

    