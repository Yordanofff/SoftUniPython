weekday_prices = [2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85]
weekend_prices = [2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20]
fruits = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]

fruit = input()
week_day = input()
quantity = float(input())

if fruit in fruits:
    fruit_index = fruits.index(fruit)
else:
    print("error")
    exit(1)

if week_day in working_days:
    print(f"{quantity * weekday_prices[fruit_index]:.2f}")
elif week_day in weekend_days:
    print(f"{quantity * weekend_prices[fruit_index]:.2f}")
else:
    print("error")