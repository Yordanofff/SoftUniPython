money_needed = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
all_sold = puzzles * 2.60 + dolls * 3 + teddy_bears * 4.10 + minions * 8.20 + trucks * 2
num_sold = puzzles + dolls + teddy_bears + minions + trucks
if num_sold >= 50:
    all_sold = all_sold * 0.75

rent = all_sold * 0.1
all_profit = all_sold - rent

if all_profit >= money_needed:
    print(f"Yes! {(all_profit - money_needed):.2f} lv left.")
else:
    print(f"Not enough money! {(money_needed - all_profit):.2f} lv needed.")