num_packets = int(input())

prices_per_ton = {"van": 200, "truck": 175, "train": 120}

tons_per_vehicle = {"van": 0, "truck": 0, "train": 0}
for i in range(num_packets):
    package_weight = int(input())
    if package_weight <= 3:
        tons_per_vehicle["van"] += package_weight
    elif package_weight <= 11:
        tons_per_vehicle["truck"] += package_weight
    else:
        tons_per_vehicle["train"] += package_weight

prices_per_vehicle = {}
for vehicle in ["van", "truck", "train"]:
    prices_per_vehicle[vehicle] = tons_per_vehicle[vehicle] * prices_per_ton[vehicle]

total_weight_tons = sum(tons_per_vehicle.values())
total_price = sum(prices_per_vehicle.values())

avg_price_per_ton = total_price / total_weight_tons
print(f"{avg_price_per_ton:.2f}")

percent_per_vehicle = {}
for vehicle in ["van", "truck", "train"]:
    percent_per_vehicle[vehicle] = tons_per_vehicle[vehicle] / total_weight_tons * 100
    print(f"{percent_per_vehicle[vehicle]:.2f}%")

