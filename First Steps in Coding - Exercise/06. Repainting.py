nylon_per_sqm = 1.5
paint_per_liter = 14.5
paint_thinner_per_liter = 5

total_paint_needed_with_extra = 1.1 * paint_per_liter
extra_nylon = 2 * nylon_per_sqm
bags = 0.4
workers_percentage = 0.3

num_nylon = int(input())
num_paint = int(input())
num_thinner = int(input())
num_hours = int(input())

materials = num_nylon * nylon_per_sqm + extra_nylon + num_paint * total_paint_needed_with_extra + num_thinner * paint_thinner_per_liter + bags
workers = materials * workers_percentage * 8

total = materials + workers
print(total)