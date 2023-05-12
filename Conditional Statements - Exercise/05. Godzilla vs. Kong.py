budget = float(input())
number_of_workers = int(input())
price_clothing = float(input())
price_decor = budget * 0.1

if number_of_workers > 150:
    price_clothing = price_clothing * 0.9

total_clothing_price = number_of_workers * price_clothing
total_spend = total_clothing_price + price_decor

if budget < total_spend:
    print("Not enough money!")
    print(f"Wingard needs {(total_spend - budget):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budget - total_spend):.2f} leva left.")