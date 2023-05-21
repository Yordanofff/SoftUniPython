from math import ceil, floor
tenis_price = float(input())
num_tenis = int(input())
num_shoes = int(input())
price_shoes = tenis_price / 6

total_price = (tenis_price * num_tenis + num_shoes * price_shoes) * 1.2  # 20% more stuff

print(f"Price to be paid by Djokovic {floor(total_price/8)}")
print(f"Price to be paid by sponsors {ceil(total_price*7/8)}")
