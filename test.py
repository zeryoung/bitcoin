# access key
# WX84pZEWXv11BRmWRqj3hfl6xyxQWYty0uSJ0R05
# Secret ke
# xhcrm3uvqNcxDNBbTyb7T4joUUiEFKj7K6nlYWD6

# pip install pyupbit

import pyupbit

access = "WX84pZEWXv11BRmWRqj3hfl6xyxQWYty0uSJ0R05"          # 본인 값으로 변경
secret = "xhcrm3uvqNcxDNBbTyb7T4joUUiEFKj7K6nlYWD6"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-XRP"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회