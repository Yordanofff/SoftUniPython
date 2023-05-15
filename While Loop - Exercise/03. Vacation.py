money_needed = float(input())
money_in_hand = float(input())

# money_to_save = money_needed - money_in_hand

num_continuous_days_spending = 0
num_days_total = 0

cmd = input()
while True:
    num_days_total += 1
    if cmd == "spend":
        num_continuous_days_spending += 1
        if num_continuous_days_spending == 5:
            print("You can't save the money.")
            print(num_days_total)
            break
        amount = float(input())
        if amount >= money_in_hand:
            money_in_hand = 0
        else:
            money_in_hand -= amount
    elif cmd == "save":
        num_continuous_days_spending = 0
        amount = float(input())
        money_in_hand += amount
        if money_in_hand >= money_needed:
            print(f"You saved the money for {num_days_total} days.")
            break
    cmd = input()