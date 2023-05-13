temp = int(input())
time_of_day = input()

outfit = "Shirt"
shoes = "Moccasins"
if time_of_day == "Morning":
    if 10 <= temp <= 18:
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < temp <= 24:
        shoes = "Moccasins"
    elif temp >= 25:
        outfit = "T-Shirt"
        shoes = "Sandals"
elif time_of_day == "Afternoon":
    if 18 < temp <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif temp >= 25:
        outfit = "Swim Suit"
        shoes = "Barefoot"

print(f"It's {temp} degrees, get your {outfit} and {shoes}.")