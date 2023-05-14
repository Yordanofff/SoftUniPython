budget = float(input())
season = input()

car_class = "Luxury class"
car_type = "Jeep"
part_of_budget = 0.9
if budget <= 100:
    car_class = "Economy class"
    car_type = "Cabrio"
    part_of_budget = 0.35
    if season == "Winter":
        car_type = "Jeep"
        part_of_budget = 0.65
elif budget <= 500:
    car_class = "Compact class"
    car_type = "Cabrio"
    part_of_budget = 0.45
    if season == "Winter":
        car_type = "Jeep"
        part_of_budget = 0.8

price = budget * part_of_budget

print(car_class)
print(f"{car_type} - {price:.2f}")
