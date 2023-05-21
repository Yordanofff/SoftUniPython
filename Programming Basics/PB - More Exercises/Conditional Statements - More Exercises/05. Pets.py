from math import ceil, floor

days = int(input())
kg_food_left = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

food_needed = (dog_food_per_day + cat_food_per_day + turtle_food_per_day) * days
diff = abs(food_needed - kg_food_left)
if food_needed < kg_food_left:
    print(f"{floor(diff)} kilos of food left.")
else:
    print(f"{ceil(diff)} more kilos of food are needed.")
