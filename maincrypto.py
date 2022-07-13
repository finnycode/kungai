import requests
import pandas
import numpy
import json
import plotly.graph_objects as go
import pandas as pd
from datetime import date
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import csv
from new_crypto import *
ticker = input("ticker ")
ticker = ticker.upper()
ticker = "X:" + ticker + "USD"
print("Program currently only supports 1 day. time is min/hour/day. range is the amount of min(1-420)/hour(1-7)/day(1).")
time = input("timespan(min, hour, day) ")
timenum = ""
if time.lower() == "min":
    timenum = 420
if time.lower() == "hour":
    timenum = 7
if time.lower() == "day":
    timenum = 1
r1 = input("range(1,5,15,30,60)")
r1 = int(r1)
r2 = int(r1)
minutes_overall = int(timenum / r1)
r1 = str(r1)
sma_inp = int(input("SMA: "))
today = str(date.today())
request_url = "https://api.polygon.io/v2/aggs/ticker/"+ ticker +"/range/1/minute/2021-07-22/"+ today +"?adjusted=true&sort=desc&limit=5000&apiKey=ZwMEsRmpnXsoTtzA2y69x7stNYQ7cY3J"

#range must be in increments of 5 and the 420 min trading day must be divided by said range eg. range of 5, 84
response = requests.get(request_url)
response = json.loads(response.content)
response = pd.DataFrame(response)
response.to_csv('hist_data.csv')


response_array = response['results']
minute1 = []
open = []
close = []
high = []
low = []
#for sup/res detection
    
# this code gets price data

for i in range(0, minutes_overall):
    minute = response['results'][i]
    minute1.append(i)
    open.append(minute['o'])
    close.append(minute['c'])
    high.append(minute['h'])
    low.append(minute['l'])


#this code calculates bollinger bands

close_dataframe = pd.DataFrame(close)





def get_sma(prices, rate):
    return prices.rolling(window = rate).mean()

def get_bollinger_bands(close_dataframe, rate=sma_inp):
    sma = get_sma(close_dataframe, rate) # <-- Get SMA for 20 days
    std = close_dataframe.rolling(rate).std() # <-- Get rolling standard deviation for 20 days
    bollinger_up = sma + std * 1.85 # Calculate top band
    bollinger_down = sma - std * 1.85 # Calculate bottom band
    return bollinger_up, bollinger_down


bollinger_up, bollinger_down = get_bollinger_bands(close_dataframe)

sma = get_sma(close_dataframe, sma_inp) # Get 20 [time_value] SMA

get_bollinger_bands(close_dataframe)


bollinger_up = bollinger_up.dropna()
bollinger_down = bollinger_down.dropna()
sma = sma.dropna()
close_dataframe1 = close_dataframe.iloc[-1].astype(float)
sma1 = sma.iloc[-1].astype(float)
close_dataframe1 = close_dataframe1[0]
sma1 = sma1[0]

print('HERE')
bb_band_arr_up = bollinger_up.values
bb_band_arr_down = bollinger_down.values

print()



iloc_index = 0
dataframe_len = (len(close_dataframe))
crossedup = 0
crosseddown = 0
price_array = close_dataframe.values
amtshares = 0
fakemoney = 100
moneymult = 0
keepgoing = True
for i in range(0,dataframe_len - 20):
    cdf1 = str(price_array[i]).lstrip('[').rstrip(']')
    cdf1 = float(cdf1)
    current_bb_up = str(bb_band_arr_up[i]).lstrip('[').rstrip(']')
    current_bb_up = float(current_bb_up)
    current_bb_down = str(bb_band_arr_down[i]).lstrip('[').rstrip(']')
    current_bb_down = float(current_bb_down)

    if cdf1 <= current_bb_down:
        crosseddown += 1
    if cdf1 >= current_bb_up:
        crossedup += 1  
    if crossedup == 2:
        print("crossed twice up!")
        crossedup = 0
    if crosseddown == 2:
        print("crossed twice down!") 
        crosseddown = 0




#print(bollinger_up)
#print(bollinger_down)


if close_dataframe1 > sma1:
    print("price is closest to the top bb band")

if close_dataframe1 < sma1:
    print("price is closest to the low bb band")




# Plot the data
plt.title(ticker + ' Bollinger Bands')
plt.xlabel('Days')
plt.ylabel('Closing Prices')
plt.plot(close_dataframe, label='Closing Prices')
plt.plot(bollinger_up, label='sma +2 standard deviation', c='g')
plt.plot(bollinger_down, label='sma -2 standard deviation', c='r')
plt.legend()
plt.show()

#this code plots price data

#fig = go.Figure(data=[go.Candlestick(x=minute1,
#                open = open,
#                high=high,
#                low=low,
#                close=close)])
#
#                
#             
#
#
#fig.show()

#fractal code in writecodeforme.py should go below this
