budget = int(input())
season = input()
people = int(input())

prices = {"Spring": 3000, "Summer": 4200, "Autumn": 4200, "Winter": 2600}

discount = 0
if people <= 6:
    discount = 0.1
elif people <= 11:
    discount = 0.15
else:
    discount = 0.25

additional_discount = 0
if people % 2 == 0 and season != "Autumn":
    additional_discount = 0.05

cost_with_discount = prices[season] * (1-discount)
cost_with_additional_discount = cost_with_discount * (1-additional_discount)

if budget >= cost_with_additional_discount:
    print(f"Yes! You have {budget - cost_with_additional_discount:.2f} leva left.")
else:
    print(f"Not enough money! You need {cost_with_additional_discount - budget:.2f} leva.")