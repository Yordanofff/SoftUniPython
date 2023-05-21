flower_type = input()
amount = int(input())
budget = int(input())

flower_prices = {"Roses": 5, "Dahlias": 3.8, "Tulips": 2.8, "Narcissus": 3, "Gladiolus": 2.5}

discount = 0
if flower_type == "Roses":
    if amount > 80:
        discount = 0.1
elif flower_type == "Dahlias":
    if amount > 90:
        discount = 0.15
elif flower_type == "Tulips":
    if amount > 80:
        discount = 0.15
elif flower_type == "Narcissus":
    if amount < 120:
        discount = -0.15
elif flower_type == "Gladiolus":
    if amount < 80:
        discount = -0.2

cost_no_discount = flower_prices[flower_type] * amount
cost_with_discount = cost_no_discount * (1 - discount)

if budget >= cost_with_discount:
    print(f"Hey, you have a great garden with {amount} {flower_type} and {budget - cost_with_discount:.2f} leva left.")
else:
    print(f"Not enough money, you need {cost_with_discount - budget:.2f} leva more.")