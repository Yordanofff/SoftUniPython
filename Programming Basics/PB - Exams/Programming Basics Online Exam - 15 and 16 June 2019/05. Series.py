budget = float(input())
series_to_buy_count = int(input())
discounts = {"Thrones": 50, "Lucifer": 40, "Protector": 30, "TotalDrama": 20, "Area": 10}

money_spend = 0
for _ in range(series_to_buy_count):
    series_name = input()
    series_price = float(input())
    if series_name in discounts:
        money_spend += series_price * (1 - discounts[series_name]/100)
    else:
        money_spend += series_price

if budget >= money_spend:
    print(f"You bought all the series and left with {budget - money_spend:.2f} lv.")
else:
    print(f"You need {money_spend - budget:.2f} lv. more to buy the series!")