calories_per_1_gram = {"fat": 9, "protein": 4, "carbs": 4}

fat = int(input())
protein = int(input())
carbs = int(input())
calories_total_required = int(input())
water_percentage = int(input())

food_weight = fat / 100 * calories_total_required / calories_per_1_gram["fat"] + (
        protein + carbs) / 100 * calories_total_required / calories_per_1_gram["protein"]

total_calories_per_1_gram = calories_total_required / food_weight

total_calories_per_1_gram_no_water = (100 - water_percentage) / 100 * total_calories_per_1_gram

print(f"{total_calories_per_1_gram_no_water:.4f}")
