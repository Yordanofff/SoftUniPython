import sys

n = int(input())
part_of_day = input()

price_per_km_day = {"taxi": 0.79, "bus": 0.09, "train": 0.06}
price_per_km_night = {"taxi": 0.9, "bus": 0.09, "train": 0.06}
starting_price = {"taxi": 0.7, "bus": 0, "train": 0}

price_per_km_to_use = price_per_km_day if part_of_day == "day" else price_per_km_night

if n >= 100:
    allowed_vehicles = list(starting_price)
elif n >= 20:
    allowed_vehicles = list(starting_price)[:2]
else:
    allowed_vehicles = list(starting_price)[:1]

lowest_price = sys.maxsize
for i in allowed_vehicles:
    price = starting_price[i] + price_per_km_to_use[i] * n
    if price < lowest_price:
        lowest_price = price

print(f"{lowest_price:.2f}")
