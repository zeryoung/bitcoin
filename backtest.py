# 투자전략 백테스팅
import pyupbit
import numpy as np


#OHLCV(opeen, high, low, clsoe, volume 자료)
df = pyupbit.get_ohlcv("KRW-BTC", count =120) #7일동안, krw-btc의 ohlcv 값을 가져오는 것
df['range'] = (df['high'] - df['low']) * 0.5 # 변동폭 * k 계산, (고가 - 저가 ) * k값
df['target'] = df['open'] + df['range'].shift(1) # target(매수가), range 컬럼을 한칸씩 밑으로 내림(.shifht(1))


fee = 0.0032 # 수수료
#  ror(수익율), np.where(조건문, 참일때 값, 거짓일때 값) : 조건문에 따라 두가지 결과 도출
df['ror'] = np.where(df['high'] > df['target'], # 고가가 타겟값보다 높으면 매수
                     df['close'] / df['target'] - fee, #종가를 목표가로 나누면 수익율
                     1) # 그외의 경우에는 매수를 안하기에 수익율은 그대로이므로 1

#누적 곱 계싼(cumprod) -> 누적 수익률(hpr)
df['hpr'] = df['ror'].cumprod()
# 하락폭 계산 Draw Down, (누적 최대 값과 현재 hpr의 차이 / 누적 최대값 *100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100
#Draw Down의 최대값 MDD를 .max()로 찾기
print("MDD(%): ", df['dd'].max())
# 결과를 엑셀로 도출
df.to_excel("dd.xlsx")