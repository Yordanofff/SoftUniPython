budget = float(input())
destination = input()
season = input()
days = int(input())

if season == "Winter":
    if destination == "Dubai":
        cost_per_day = 45000
    elif destination == "Sofia":
        cost_per_day = 17000
    elif destination == "London":
        cost_per_day = 24000
elif season == "Summer":
    if destination == "Dubai":
        cost_per_day = 40000
    elif destination == "Sofia":
        cost_per_day = 12500
    elif destination == "London":
        cost_per_day = 20250

discount = 0
if destination == "Dubai":
    discount = 0.30
elif destination == "Sofia":
    discount = -0.25

price_no_disc = cost_per_day * days
price_total = price_no_disc - price_no_disc * discount

if budget >= price_total:
    print(f"The budget for the movie is enough! We have {budget - price_total:.2f} leva left!")
else:
    print(f"The director needs {price_total - budget:.2f} leva more!")