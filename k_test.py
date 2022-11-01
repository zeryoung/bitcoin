import pyupbit
import numpy as np

def get_ror(k=0.5):
    df = pyupbit.get_ohlcv("KRW-BTC")
    df['range'] = (df['high'] - df['low']) * k
    df['target'] = df['open'] + df['range'].shift(1)

    fee = 0.0032
    df['ror'] = np.where(df['open'] < df['target'], # 고가가 타겟값보다 높으면 매수
                        df['target'] / df['open'] - fee, #종가를 목표가로 나누면 수익율
                        1) # 그외의 경우에는 매수를 안하기에 수익율은 그대로이므로 1

    ror = df['ror'].cumprod()[-2]
    return ror


for k in np.arange(0.1, 1.0, 0.05):
    ror = get_ror(k)
    print("%.1f %f" % (k, ror))