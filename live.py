from operator import is_
from this import d
import time
import requests, json
import alpaca_trade_api as api


#API_KEY = "PK247079F97UUO0ITDG5"
#BASE_URL = "https://paper-api.alpaca.markets"
#API_SECRET = "HRuVMCARBN3i4gyyA75YjI7fV8FxvttyzsGcHfhg"
#
#alpaca = api.REST(API_KEY, API_SECRET, BASE_URL)
#
#account = alpaca.get_account()
#print(account)
#
#symbol = "BTC/USD"
#qty = 1
#
#side = "buy"
#type = "market"
#time_in_force = "ioc"





from glob import glob
from hashlib import new
from types import new_class
from matplotlib.animation import FuncAnimation
import websocket
import json
import matplotlib.animation as animation
import bokeh as b
from bokeh.plotting import figure, show
import yaml
#from config import *

import pandas as pd
import time as t
import matplotlib.pyplot as plt
import csv
import os

numb = ""
p = ""
message_gotten = False
bollinger_up = []
bollinger_down = []
close_dataframe = [25000]
lemon = 0
sma_inp = 10
buy_money = 10000
hist_port_value = []

#sell_money = 5000
#codes_sma = input("SMA: ")
#standard_deviation = input("Standard deviation(1.0-2.0): ")
#ticker = input("Either BTC or ETH: ")
#loop_grah = 0
#anothaclose = []
#if ticker.upper() == "BTC":
#    loop_grah = 11
#if ticker.upper() == "ETH":
#    loop_grah = 9

#get websocket DATA
def on_open(ws):
    print("opened")
    auth_data = {"action":"auth", "params":"ZwMEsRmpnXsoTtzA2y69x7stNYQ7cY3J"}

    ws.send(json.dumps(auth_data))

    channel_data = {"action":"subscribe", "params":"XA.X:ETH-USD"}

    ws.send(json.dumps(channel_data))


notswag = True
add_mult = 0
gay = True
new_string = ""
messagecnt = 0
add_mult = 2
brah = ""
gay = True
grah = ""
xyeah = []
weee = "" 
for i in range(0, 100):
    xyeah.append(i)
ocounter = 0
messagcnt = 0
ya_motha = 0

def get_sma(prices, rate):
    return prices.rolling(window = rate).mean()


loop_num = 0
bought = False
sold = False
buy_price = 0
short_price = 0
short_price2 = 0
buy_price2 = 0
sold_price2 = 0
sold2 = False
bought2 = False
bought_back_price = 0
sold_price = 0
sold_price2 = 0
total_profit = 0
is2 = 0
bad_above = 0
bad_below = 0
good_below = 0
good_above = 0
is2_val = 2
bad_buy = 0
bad_sell = 0
safe_money = 717
def get_bollinger_bands(close_dataframe, rate=sma_inp):
    global loop_num, bought, bad_buy, safe_money, bad_sell, sold, sold2, bought2, sold_price2, good_above, is2_val, good_below, hist_port_value, short_price2, buy_price2, buy_price, buy_money, short_price, is2, sold_price, bought_back_price, total_profit, bad_above, bad_below
    sma = get_sma(close_dataframe, rate) # <-- Get SMA for 20 days
    std = close_dataframe.rolling(rate).std() # <-- Get rolling standard deviation for 20 days
    bollinger_up = sma + std * 1.85 # Calculate top band
    bollinger_down = sma - std * 1.85 # Calculate bottom band
    new_bbup= []
    new_bbdown = []
    bollinger_up = bollinger_up.values
    bollinger_down = bollinger_down.values
    sma = sma.values
    for i in range(0, len(bollinger_down)):
        new_bbdown.append(float(str(bollinger_down[i]).lstrip('[').rstrip(']')))
    for i in range(0, len(bollinger_up)):
        new_bbup.append(float(str(bollinger_up[i]).lstrip('[').rstrip(']')))
    #print("bbup = " + str(new_bbup))
    #print("bbdown = " + str(new_bbdown))
    doop = 0
    the_great_arr = []
    for i in range(0, len(close_dataframe)):
        doop+=1
        the_great_arr.append(doop)
    x = the_great_arr

    current_bb_up = bollinger_up[-1]
    current_bb_down = bollinger_down[-1]
    current_price = price_list[-1]
    is2 += 1
    print("is2 " + str(is2))
    if sold == True and is2 == is2_val:
        is2 = 0
        sold = False
        print("This trades profit = $" + str((buy_money/short_price) * (short_price-current_price)))
        total_profit += (buy_money/short_price) * (short_price-current_price)
        buy_money += (buy_money/short_price) * (short_price-current_price)
        print("Total profit = " + str(total_profit))
        #hist_port_value.append(buy_money)
        #print("Historical portfolio value = ")
        #print(hist_port_value)
        print("This trade occured at the " + str(len(price_list)) + " minutes")
        if current_price > short_price:
            bad_above += 1
        
        #if current_price > current_bb_up:
        #    print("sell")
        #    short_price = current_price
        #    sold = True
        #    is2 = 0
        #if current_price < current_bb_down:
        #    print("buy")
        #    buy_price = current_price
        #    bought = True
        #    is2 = 0

    if bought == True and is2 == is2_val:
        is2 = 0
        bought = False
        print("This trades profit = $" + str((buy_money/buy_price) * (current_price-buy_price)))
        total_profit += (buy_money/buy_price) * (current_price-buy_price)
        buy_money += (buy_money/buy_price) * (current_price-buy_price)
        print("Total profit = " + str(total_profit))
        #hist_port_value.append(buy_money)
        #print("Historical portfolio value = ")
        #print(hist_port_value)
        print("This trade occured at the " + str(len(price_list)) + " minute")
        if current_price < buy_price:
            bad_below += 1
        #order = alpaca.submit_order("ETHUSD", 9.9755, 'sell', "market", "ioc")
        #if current_price > current_bb_up:
        #    print("sell")
        #    short_price = current_price
        #    sold = True
        #    is2 = 0
        #if current_price < current_bb_down:
        #    print("buy")
        #    buy_price = current_price
        #    bought = True
        #    is2 = 0

    if bad_sell == True:
        print("This trades profit = $" + str((buy_money/short_price) * (short_price-current_price)))
        total_profit += (buy_money/short_price) * (short_price-current_price)
        buy_money += (buy_money/short_price) * (short_price-current_price)
        print("Total profit = " + str(total_profit))
        #hist_port_value.append(buy_money)
        #print("Historical portfolio value = ")
        #print(hist_port_value)
        print("This trade occured at the " + str(len(price_list)) + " minutes")
        if current_price > short_price:
            bad_above += 1
    if bad_buy == True:
        print("This trades profit = $" + str((buy_money/buy_price) * (current_price-buy_price)))
        total_profit += (buy_money/buy_price) * (current_price-buy_price)
        buy_money += (buy_money/buy_price) * (current_price-buy_price)
        print("Total profit = " + str(total_profit))
        #hist_port_value.append(buy_money)
        #print("Historical portfolio value = ")
        #print(hist_port_value)
        print("This trade occured at the " + str(len(price_list)) + " minute")
        if current_price < buy_price:
            bad_below += 1



    
    if current_price > current_bb_up and sold == False and bad_above < 3:
        bad_above = 0
        print("sell")
        short_price = current_price
        sold = True
        is2 = 0
        #order = alpaca.submit_order("ETHUSD", 10, 'sell', "market", "ioc")
        #p = figure(title="Simple line example", x_axis_label='min', y_axis_label='price')
        #p.line(x, new_bbdown, legend_label="bbdown", line_width=2, color='red')
        #p.line(x, price_list, legend_label="price", line_width=2, color='blue')
        #p.line(x, new_bbup, legend_label="bbup", line_width=2, color='green')
        #show(p)
    
    if current_price < current_bb_down and bought == False and bad_below < 3:
        bad_below = 0
        print("buy")
        buy_price = current_price
        bought = True
        is2 = 0
        #order = alpaca.submit_order("ETHUSD", 10, 'buy', "market", "ioc")
        #p = figure(title="Simple line example", x_axis_label='min', y_axis_label='price')
        #p.line(x, new_bbdown, legend_label="bbdown", line_width=2, color='red')
        #p.line(x, price_list, legend_label="price", line_width=2, color='blue')
        #p.line(x, new_bbup, legend_label="bbup", line_width=2, color='green')
        #show(p)
    
    if current_price < short_price and bad_above > 2:
        #is2_val = 4
        good_above += 1
    if good_above > 2:
        bad_above = 0
    if current_price > buy_price and bad_below > 2:
        good_below += 1
    if good_above > 2:
        bad_below = 0


    if sold == False and bad_below > 2:
        bad_sell = True
        print("sell")
        short_price = current_price
    if bought == False and bad_above > 2:
        bad_buy = True
        print("sell")
        buy_price = current_price
    print("Bad Below value = " + str(bad_below))
    print("Bad Above value = " + str(bad_above))
    print("Good Below value = " + str(good_below))
    print("Good Above value = " + str(good_above))
    
   
    print("Buy money = " + str(buy_money))
    #print("Sell money = " + str(sell_money))
    p = figure(title="Simple line example", x_axis_label='min', y_axis_label='price')
    p.line(x, new_bbdown, legend_label="bbdown", line_width=2, color='red')
    p.line(x, price_list, legend_label="price", line_width=2, color='blue')
    p.line(x, new_bbup, legend_label="bbup", line_width=2, color='green')
    

#second bbbabd func

    
    sma2 = get_sma(close_dataframe, 5) # <-- Get SMA for 20 days
    std2 = close_dataframe.rolling(5).std() # <-- Get rolling standard deviation for 20 days
    bollinger_up2 = sma2 + std2 * 1 # Calculate top band
    bollinger_down2 = sma2 - std2 * 1 # Calculate bottom band
    new_bbup2= []
    new_bbdown2= []
    bollinger_up2 = bollinger_up2.values
    bollinger_down2 = bollinger_down2.values
    sma2 = sma2.values
    for i in range(0, len(bollinger_down2)):
        new_bbdown2.append(float(str(bollinger_down2[i]).lstrip('[').rstrip(']')))
    for i in range(0, len(bollinger_up2)):
        new_bbup2.append(float(str(bollinger_up2[i]).lstrip('[').rstrip(']')))
    #print("bbup = " + str(new_bbup))
    #print("bbdown = " + str(new_bbdown))
    doop = 0
    the_great_arr = []
    for i in range(0, len(close_dataframe)):
        doop+=1
        the_great_arr.append(doop)
    x = the_great_arr

    current_bb_up2 = bollinger_up2[-1]
    current_bb_down2 = bollinger_down2[-1]
    current_price2 = price_list[-1]
    
    if sold2 == True:
        sold2 = False
        print("This trades profit = $" + str((buy_money/short_price2) * (short_price2-current_price2)))
        total_profit += (buy_money/short_price2) * (short_price2-current_price2)
        buy_money += (buy_money/short_price2) * (short_price2-current_price2)
        print("Total profit = " + str(total_profit))
        #hist_port_value.append(buy_money)
        #print("Historical portfolio value = ")
        #print(hist_port_value)
        print("This trade occured at the " + str(len(price_list)) + " minute")
        #if current_price > current_bb_up:
        #    print("sell")
        #    short_price = current_price
        #    sold = True
        #    is2 = 0
        #if current_price < current_bb_down:
        #    print("buy")
        #    buy_price = current_price
        #    bought = True
        #    is2 = 0

    if bought2 == True:
        bought2 = False
        print("This trades profit = $" + str((buy_money/buy_price2) * (current_price2-buy_price2)))
        total_profit += (buy_money/buy_price2) * (current_price2-buy_price2)
        buy_money += (buy_money/buy_price2) * (current_price2-buy_price2)
        print("Total profit = " + str(total_profit))
        #hist_port_value.append(buy_money)
        #print("Historical portfolio value = ")
        #print(hist_port_value)
        print("This trade occured at the " + str(len(price_list)) + " minute")
        #order = alpaca.submit_order("ETHUSD", 9.9755, 'sell', "market", "ioc")
        #if current_price > current_bb_up:
        #    print("sell")
        #    short_price = current_price
        #    sold = True
        #    is2 = 0
        #if current_price < current_bb_down:
        #    print("buy")
        #    buy_price = current_price
        #    bought = True
        #    is2 = 0

    
    if current_price2 > current_bb_up2 and sold2 == False:
        print("sell")
        short_price2 = current_price2
        sold2 = True
        #p = figure(title="Simple line example", x_axis_label='min', y_axis_label='price')
        #p.line(x, new_bbdown, legend_label="bbdown", line_width=2, color='red')
        #p.line(x, price_list, legend_label="price", line_width=2, color='blue')
        #p.line(x, new_bbup, legend_label="bbup", line_width=2, color='green')
        #show(p)
    
    if current_price2 < current_bb_down2 and bought2 == False:
        print("buy")
        buy_price2 = current_price2
        bought2 = True
        #order = alpaca.submit_order("ETHUSD", 10, 'buy', "market", "ioc")
        
        #p = figure(title="Simple line example", x_axis_label='min', y_axis_label='price')
        #p.line(x, new_bbdown, legend_label="bbdown", line_width=2, color='red')
        #p.line(x, price_list, legend_label="price", line_width=2, color='blue')
        #p.line(x, new_bbup, legend_label="bbup", line_width=2, color='green')
        #show(p)
    
        
    
   
    print("Buy money = " + str(buy_money))
    #print("Sell money = " + str(sell_money))
    #print("Safe money: " + str(safe_money))
    p.line(x, new_bbdown2, legend_label="1 standard dev bel", line_width=2, color='black')
    p.line(x, price_list, legend_label="price", line_width=2, color='blue')
    p.line(x, new_bbup2, legend_label="1 standard dev above", line_width=2, color='black')
    #show(p)
    return bollinger_up, bollinger_down
    




   
grunk = 1
buyindex = 0
price_list = []
def add_tol(newahprice):
    price_list.append(newahprice)
    #print(price_list)

l5 = []
val_5 = 0
got_it = False
is_5 = False
def on_message(ws, message):
    global is2
    global l5
    global val_5
    global grunk
    data = message
    
    data = str(data)
    data = list(data)
    grah = ""
    weee = ""
    ya_motha = 0
    for thing in data:
        if thing == "o":
            for i in range(0,10):
                grah = grah.join(data[ya_motha])
                weee = weee + grah
                ya_motha += 1  
        ya_motha += 1    
    



    weee = weee.lstrip("o") 
    weee = weee.lstrip("\"")
    weee = weee.lstrip(":")
    weee = float(weee)
   
    print(weee)
    print("minutes = " + str(grunk))
    grunk+=1
   
    add_tol(weee)
   
    
    
    if len(price_list) >= 1:
        get_sma(pd.DataFrame(price_list), rate=5)
        get_bollinger_bands(pd.DataFrame(price_list))
        
    #l5.append(weee)
    #if len(l5) == 5:
    #    for val in l5:
    #        val_5 += val
    #    val_5 /= 5
    #    l5 = []
    #    is_5 = True
    #if is_5 == True:
    #    add_tol(val_5)
    #    val_5 = 0
#
    #
    
    
 
                
        
socket =  "wss://socket.polygon.io/crypto"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()








