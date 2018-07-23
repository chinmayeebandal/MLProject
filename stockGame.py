#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 00:01:24 2018

@author: cbandal
"""

import stockGraphs as sg

class simulator:
    
    balance = float(10000); #each player begins with $10,000 in their account
    stocks = {} #dictionary
    #print(stocks)
    
    #def __init__(self, name):
    #    self.name = name
    #    self.balance = 10000 
        
    
    name = input("Enter your name: ")
    tickers = input("Which stocks are you interested in? ").split(' ')
    date_range = input("Date range YYYY-MM-DD: ").split(' ')
    #see stock market
    for tick in tickers:
        print(tick)
        sg.printGraph(tick, date_range[0], date_range[1]) #gives general info
        
    #trade stocks
    trade = input("Trade stock? y/n: ")
    while(trade == 'y'): 
        order = input("Stock order? Transaction, Stock symbol, Quantity: ").split(' ')
        if(order[0] == "buy"):
            ticker = order[1]
            sg.printGraph(ticker, date_range[0], date_range[1]) #gives general info
            close = sg.getClosingPrice(ticker, date_range[0], date_range[1])
            cost = close * int(order[2])
            if(balance - cost <= 1000):
                print("Insufficient funds")
                trade = input("Trade stock? y/n: ")
            else:
                balance -= cost
                print("Account value: ", balance)
        
                if(stocks.get(ticker) == None):
                    stocks[ticker] = int(order[2])
                else:
                    stocks[ticker] += int(order[2])
                print(stocks.items())
                trade = input("Trade stock? y/n: ")
            
        elif(order[0] == "sell"):
            ticker = order[1]
            if(stocks.get(ticker) == None):
                print(ticker," not found in your trade")
                trade = input("Trade stock? y/n: ")
            else:
                #sg.printGraph(ticker, date_range[0], date_range[1]) #gives general info
                close = sg.getClosingPrice(ticker, date_range[0], date_range[1])
                cost = close * int(order[2])
                balance += cost
                print("Account value: ", balance)
                
                diff = stocks[ticker] - int(order[2])
                if(diff > 1):
                    stocks[ticker] = diff
                else:
                    stocks.pop(ticker)
                print(stocks.items())
                trade = input("Trade stock? y/n: ")
                
    if(trade == "n"):
        prediction = input("Predictions of stocks? y/n: ") #stock predictions
        if(prediction == "y"):
            pred = input("Enter stock name, start date and end date: ").split(' ')
            ticker = pred[0]
            start = pred[1]
            end = pred[2]
            sg.stockPrediction(ticker, start, end)
            
            summary = input("Summary? y/n: ") #Summary 
            if(summary == "y"):
                print("Account balance: ", balance)
                for ticks in stocks:
                    print(ticks, " Quantity: ",stocks[ticks], " Close: ", sg.getClosingPrice(ticker, date_range[0], date_range[1]))
                annual_return = ((balance/10000)**(365))-1
                print("Annual Return: ", annual_return)
                print("Thank you for playing, ",name,"!")
            else:
                print("Thank you for playing, ",name,"!")
                
        else:
            summary = input("Summary? y/n: ")
            if(summary == "y"):
                print("Account balance: ", balance)
                for ticks in stocks:
                    print(ticks, " Quantity: ",stocks[ticks], " Close: ", sg.getClosingPrice(ticker, date_range[0], date_range[1]))
                annual_return = ((balance/10000)**(365))-1
                print("Annual Return: ", annual_return)
                print("Thank you for playing, ",name, "!")
            else:
                print("Thank you for playing, ",name, "!")
                
    
                
        
        
    
           
        
    
    
    
    
    
        

    
