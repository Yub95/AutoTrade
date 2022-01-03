import time
import pyupbit
import datetime

def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2)
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price 

def get_start_time(ticker):
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1)
    start_time = df.index[0]
    return start_time

def get_ma5(ticker):
    """5일 이동 평균선 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=5)
    ma5 = df['open'].rolling(5).mean().iloc[-1]
    return ma5

def get_start_price(ticker) : 
    """ 시가 조회"""
    df=pyupbit.get_ohlcv(ticker,interval="day",count=1)
    start_price = df['open'].iloc[-1]
    return start_price


btc_target_price = get_target_price("KRW-BTC", 0.4)
btc_start_price = get_start_price("KRW-BTC")
btc_ma5 = get_ma5("KRW-BTC")
print('BTC : ', btc_target_price, end=' ')
if btc_ma5 < btc_start_price:
    print('개장')
else:
    print('휴장')


eth_target_price = get_target_price("KRW-ETH", 0.4)
eth_start_price = get_start_price("KRW-ETH")
eth_ma5 = get_ma5("KRW-ETH")
print('ETH : ', eth_target_price, end=' ')
if eth_ma5 < eth_start_price:
    print('개장')
else:
    print('휴장')
    
ada_target_price = get_target_price("KRW-ADA", 0.5)
ada_start_price = get_start_price("KRW-ADA")
ada_ma5 = get_ma5("KRW-ADA")
print('ADA : ', ada_target_price, end=' ')
if ada_ma5 < ada_start_price:
    print('개장')
else:
    print('휴장')


sand_target_price = get_target_price("KRW-SAND", 0.5)
sand_start_price = get_start_price("KRW-SAND")
sand_ma5 = get_ma5("KRW-SAND")
print('SAND : ', sand_target_price, end=' ')
if sand_ma5 < sand_start_price:
    print('개장')
else:
    print('휴장')

