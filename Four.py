import time
import pyupbit
import datetime

access = "reXf1Lxdxlvd5uzsFIKts1ZaCWG5DfyVAGVxcEde"
secret = "wnmgJJDyHzMcpQRGbapuTGmVj1b77WaMzPFPR4pT"

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
    return start_time

def get_balance(ticker):
    """잔고 조회"""
    balances = upbit.get_balances()
    for b in balances:
        if b['currency'] == ticker:
            if b['balance'] is not None:
                return float(b['balance'])
            else:
                return 0
    return 0
def get_current_price(ticker):
    """현재가 조회"""
    return pyupbit.get_orderbook(ticker=ticker)["orderbook_units"][0]["ask_price"]

# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매
while True:
    try:
        now = datetime.datetime.now()
        start_time = get_start_time("KRW-ETH")  #9:00
        end_time = start_time + datetime.timedelta(days=1)  #9:00 + 1일
        krw = get_balance("KRW")

    #ETH
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            eth = get_balance("ETH")
            eth_target_price = get_target_price("KRW-ETH", 0.4)
            eth_ma5 = get_ma5("KRW-ETH")
            eth_current_price = get_current_price("KRW-ETH")
            eth_start_price = get_start_price("KRW-ETH")
            if eth_target_price < eth_current_price and eth_ma5 < eth_start_price and eth < 0.000001:
                if krw > 5000:
                    upbit.buy_market_order("KRW-ETH", krw*0.1995)
        else:
            eth = get_balance("ETH")
            if eth > 0.00000001:
                upbit.sell_market_order("KRW-ETH", eth)

    #BTC
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            btc = get_balance("BTC")
            btc_target_price = get_target_price("KRW-BTC", 0.4)
            btc_ma5 = get_ma5("KRW-BTC")
            btc_current_price = get_current_price("KRW-BTC")
            btc_start_price = get_start_price("KRW-BTC")
            if btc_target_price < btc_current_price and btc_ma5 < btc_start_price and btc < 0.000001:
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTC", krw*0.1995)
        else:
            btc = get_balance("BTC")
            if btc > 0.00000001:
                upbit.sell_market_order("KRW-BTC", btc)

    #ADA
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            ada = get_balance("ADA")
            ada_target_price = get_target_price("KRW-ADA", 0.5)
            ada_ma5 = get_ma5("KRW-ADA")
            ada_current_price = get_current_price("KRW-ADA")
            ada_start_price = get_start_price("KRW-ADA")
            if ada_target_price < ada_current_price and ada_ma5 < ada_start_price and ada < 0.1:
                if krw > 5000:
                    upbit.buy_market_order("KRW-ADA", krw*0.1995)
        else:
            ada = get_balance("ADA")
            if ada > 0.00000001:
                upbit.sell_market_order("KRW-ADA", ada)


    #SAND
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            sand = get_balance("SAND")
            sand_target_price = get_target_price("KRW-SAND", 0.5)
            sand_ma5 = get_ma5("KRW-SAND")
            sand_current_price = get_current_price("KRW-SAND")
            sand_start_price = get_start_price("KRW-SAND")
            if sand_target_price < sand_current_price and sand_ma5 < sand_start_price and sand < 1:
                if krw > 5000:
                    upbit.buy_market_order("KRW-SAND", krw*0.1995)
        else:
            sand = get_balance("SAND")
            if sand > 0.00000001:
                upbit.sell_market_order("KRW-SAND", sand)


    #SOL
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            sol = get_balance("SOL")
            sol_target_price = get_target_price("KRW-SOL", 0.5)
            sol_ma5 = get_ma5("KRW-SOL")
            sol_current_price = get_current_price("KRW-SOL")
            sol_start_price = get_start_price("KRW-SOL")
            if sol_target_price < sol_current_price and sol_ma5 < sol_start_price and sol < 0.00001:
                if krw > 5000:
                    upbit.buy_market_order("KRW-SOL", krw*0.1995)
        else:
            sol = get_balance("SOL")
            if sol > 0.00000001:
                upbit.sell_market_order("KRW-SOL", sol)

        time.sleep(1)
        
    except Exception as e:
        print(e)
        time.sleep(1)
