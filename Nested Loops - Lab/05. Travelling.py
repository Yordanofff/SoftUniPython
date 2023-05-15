destination = input()
money_required = float(input())

money_collected = 0
while True:
    cmd_digit_or_city = input()
    if cmd_digit_or_city == "End":
        break
    try:
        money_collected += float(cmd_digit_or_city)
        if money_collected >= money_required:
            print(f"Going to {destination}!")
            # money_collected = money_collected - money_required
            # Lol - SoftUni at it's best :) Consider that she spent all her money when she was on holiday!
            money_collected = 0
    except:
        destination = cmd_digit_or_city
        money_required = float(input())
