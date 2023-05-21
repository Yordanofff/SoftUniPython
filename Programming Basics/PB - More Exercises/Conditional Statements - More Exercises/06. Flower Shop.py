from math import ceil, floor

TAX = 0.05
prices = {"magnolia": 3.25, "hyacinth": 4, "rose": 3.5, "cactus": 8}

num_magnolia = int(input())
num_hyacinth = int(input())
num_rose = int(input())
num_cactus = int(input())
money_needed = float(input())

price = num_magnolia * prices["magnolia"] + \
        num_hyacinth * prices["hyacinth"] + \
        num_rose * prices["rose"] + \
        num_cactus * prices["cactus"]

money_in_pocket = price - price * TAX

diff = abs(money_needed - money_in_pocket)
if money_needed > money_in_pocket:
    print(f"She will have to borrow {ceil(diff)} leva.")
else:
    print(f"She is left with {floor(diff)} leva.")
