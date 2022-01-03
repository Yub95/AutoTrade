import time
import pyupbit
import datetime

def get_target_price(ticker, k):
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price 

btc_target_price = get_target_price("KRW-BTC", 0.4)
print('BTC : ', btc_target_price)


eth_target_price = get_target_price("KRW-ETH", 0.4)
print('ETH : ', eth_target_price)

ada_target_price = get_target_price("KRW-ADA", 0.5)
print('ADA : ', ada_target_price)

sand_target_price = get_target_price("KRW-SAND", 0.5)
print('SAND : ', sand_target_price)
