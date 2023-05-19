from math import ceil, floor

vineyard_sqm = int(input())
grapes_per_sqm = float(input())
wine_needed = int(input())
num_workers = int(input())

grapes_used_for_wine = vineyard_sqm * 0.4 * grapes_per_sqm
grapes_needed_for_1_liter_wine = 2.5  # kg
wine_created = grapes_used_for_wine / grapes_needed_for_1_liter_wine

if wine_created >= wine_needed:
    diff = wine_created - wine_needed
    wine_per_worker = diff / num_workers
    print(f"Good harvest this year! Total wine: {floor(wine_created)} liters.")
    print(f"{ceil(diff)} liters left -> {ceil(wine_per_worker)} liters per person.")
else:
    print(f"It will be a tough winter! More {floor(wine_needed - wine_created)} liters wine needed.")
