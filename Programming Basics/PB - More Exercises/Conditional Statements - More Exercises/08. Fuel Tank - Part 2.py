FUEL_PRICES = {"Diesel": 2.33, "Gasoline": 2.22, "Gas": 0.93}
FUEL_DISCOUNT = {"Diesel": 0.12, "Gasoline": 0.18, "Gas": 0.08}

fuel_type = input()
amount_fuel = float(input())
discount_card = input()

is_discount = True if discount_card == "Yes" else False

extra_discount = 0
if 20 <= amount_fuel <= 25:
    extra_discount = 0.08
elif amount_fuel > 25:
    extra_discount = 0.1

price = FUEL_PRICES[fuel_type] * amount_fuel

if is_discount:
    price -= FUEL_DISCOUNT[fuel_type] * amount_fuel

# Apply extra discount
price = price * (1 - extra_discount)

print(f"{price:.2f} lv.")

