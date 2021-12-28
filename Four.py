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
    ma55 = df['close'].rolling(5).mean().iloc[-1]
    return ma55

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
        start_time = get_start_time("KRW-XLM")
        end_time = start_time + datetime.timedelta(days=1)
        krw = get_balance("KRW")

    #XLM
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            xlm_target_price = get_target_price("KRW-XLM", 0.5)
            xlm_ma5 = get_ma5("KRW-XLM")
            xlm_current_price = get_current_price("KRW-XLM")
            if xlm_target_price < xlm_current_price and xlm_ma5 < xlm_current_price:
                if krw > 5000:
                    upbit.buy_market_order("KRW-XLM", krw*0.2495)
        else:
            xlm = get_balance("XLM")
            if xlm > 0.00000001:
                upbit.sell_market_order("KRW-XLM", xlm*0.9995)

    #BTG
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            btg_target_price = get_target_price("KRW-BTG", 0.5)
            btg_ma5 = get_ma5("KRW-BTG")
            btg_current_price = get_current_price("KRW-BTG")
            if btg_target_price < btg_current_price and btg_ma5 < btg_current_price:
                if krw > 5000:
                    upbit.buy_market_order("KRW-BTG", krw*0.2495)
        else:
            btg = get_balance("BTG")
            if btg > 0.00000001:
                upbit.sell_market_order("KRW-BTG", btg*0.9995)

    #ADA
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            ada_target_price = get_target_price("KRW-ADA", 0.5)
            ada_ma5 = get_ma5("KRW-ADA")
            ada_current_price = get_current_price("KRW-ADA")
            if ada_target_price < ada_current_price and ada_ma5 < ada_current_price:
                if krw > 5000:
                    upbit.buy_market_order("KRW-ADA", krw*0.2495)
        else:
            ada = get_balance("ADA")
            if ada > 0.00000001:
                upbit.sell_market_order("KRW-ADA", ada*0.9995)


    #LTC
        if start_time < now < end_time - datetime.timedelta(minutes=140):
            ltc_target_price = get_target_price("KRW-LTC", 0.5)
            ltc_ma5 = get_ma5("KRW-LTC")
            ltc_current_price = get_current_price("KRW-LTC")
            if ltc_target_price < ltc_current_price and ltc_ma5 < ltc_current_price:
                if krw > 5000:
                    upbit.buy_market_order("KRW-LTC", krw*0.2495)
        else:
            ltc = get_balance("LTC")
            if ltc > 0.00000001:
                upbit.sell_market_order("KRW-LTC", ltc*0.9995)



        time.sleep(1)
    except Exception as e:
        print(e)
        time.sleep(1)
