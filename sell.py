import time
import pyupbit
import datetime

# access key
# WX84pZEWXv11BRmWRqj3hfl6xyxQWYty0uSJ0R05
# Secret ke
# xhcrm3uvqNcxDNBbTyb7T4joUUiEFKj7K6nlYWD6

access = "WX84pZEWXv11BRmWRqj3hfl6xyxQWYty0uSJ0R05"
secret = "xhcrm3uvqNcxDNBbTyb7T4joUUiEFKj7K6nlYWD6"

# ticker는 목표 종목, k는 희망하는 k값
def get_target_price(ticker, k):
    """변동성 돌파 전략으로 매수 목표가 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=2) # 이틀치 데이터를 활용해서 변동성 돌파 전략 채택
    target_price = df.iloc[0]['close'] + (df.iloc[0]['high'] - df.iloc[0]['low']) * k
    return target_price

#시간 가져오는 함수 설정
def get_start_time(ticker): 
    """시작 시간 조회"""
    df = pyupbit.get_ohlcv(ticker, interval="day", count=1) # 일봉으로 조회시 시작시간이 0900으로 나오는데 그 시간을 가져오는 것
    start_time = df.index[0] # ohlcv의 첫번째 값이 시간값이므로 그걸 가져옴
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


print(datetime.datetime.now())
# 로그인
upbit = pyupbit.Upbit(access, secret)
print("autotrade start")

# 자동매매 시작
# while True:
#     try:
#         # 시간 설정
#         now = datetime.datetime.now()
#         start_time = get_start_time("KRW-BTC")
#         end_time = start_time + datetime.timedelta(days=1) # 끝나는 시간은 다음날 0900시
#         #시간에 따라서 if문
#         if start_time < now < end_time - datetime.timedelta(seconds=10): # 09시로 하면 무한루프가 되니까 다음날 08시 59분 50초까지만 작동하게 만듬
#             target_price = get_target_price("KRW-BTC", 0.5)
#             current_price = get_current_price("KRW-BTC")
#             if target_price < current_price:
#                 krw = get_balance("KRW")
#                 if krw > 5000:
#                     upbit.buy_market_order("KRW-BTC", krw*0.9995)
#         else: # 당일 종가에 전량 매도
#             btc = get_balance("BTC")
#             if btc > 0.00008:
#                 upbit.sell_market_order("KRW-BTC", btc*0.9995)
#         time.sleep(1)
#     except Exception as e:
#         print(e)
#         time.sleep(1)