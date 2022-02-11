import pyupbit
import pandas as pd

BTC = pyupbit.get_ohlcv("KRW-BTC","day",count=600,period=0.1)
ETH = pyupbit.get_ohlcv("KRW-ETH", "day", count = 600, period = 0.1)
SOL = pyupbit.get_ohlcv("KRW-SOL","day",count=600,period=0.1)
SAND = pyupbit.get_ohlcv("KRW-SAND", "day", count = 600, period = 0.1)
ADA = pyupbit.get_ohlcv("KRW-ADA","day",count=600,period=0.1)
df= pd.DataFrame({'BTC' : BTC['close'], 'ETH' : ETH['close'], 'SOL' : SOL['close'], 'SAND' : SAND['close'], 'ADA' : ADA['close']})

print(df.corr())
