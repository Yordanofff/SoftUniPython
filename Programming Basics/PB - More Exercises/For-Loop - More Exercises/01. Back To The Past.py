money = float(input())
year_to_live_to = int(input())

SPEND_PER_EVEN_YEAR = 12_000
STARTING_YEAR = 1800
y_old = 18
for i in range(STARTING_YEAR, year_to_live_to + 1):
    money -= SPEND_PER_EVEN_YEAR
    if i % 2 == 1:
        money -= y_old * 50
    y_old += 1

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {-money:.2f} dollars to survive.")
