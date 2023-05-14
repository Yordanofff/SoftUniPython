def truck_driver(season, km_per_m):
    prices_5k = {"Spring": 0.75, "Autumn": 0.75, "Summer": 0.9, "Winter": 1.05}
    prices_10k = {"Spring": 0.95, "Autumn": 0.95, "Summer": 1.1, "Winter": 1.25}
    price_10_20k = 1.45

    tax = 0.1
    if km_per_m <= 5000:
        salary = prices_5k[season] * km_per_m
    elif km_per_m <= 10000:
        salary = prices_10k[season] * km_per_m
    else:
        salary = price_10_20k * km_per_m

    salary_with_tax = salary * (1 - tax) * 4
    print(f"{salary_with_tax:.2f}")


s = input()
km_pm = float(input())

truck_driver(s, km_pm)
