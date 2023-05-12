chicken = 10.35
fish = 12.40
vegan = 8.15

delivery = 2.5

num_chicken = int(input())
num_fish = int(input())
num_vegan = int(input())
total_meal = num_chicken * chicken + num_fish * fish + num_vegan * vegan
desert = total_meal * 0.2

total = total_meal + desert + delivery
print(total)