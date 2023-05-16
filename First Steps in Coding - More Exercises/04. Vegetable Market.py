price_veggies = float(input())
price_fruits = float(input())
veggies_kg = int(input())
fruits_kg = int(input())

EUR = 1.94

total_price = price_fruits * fruits_kg + price_veggies * veggies_kg
total_price_EUR = total_price / EUR
print(f"{total_price_EUR:.2f}")
