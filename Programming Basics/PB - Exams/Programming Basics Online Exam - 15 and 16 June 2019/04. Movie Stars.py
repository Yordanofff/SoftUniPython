budget = float(input())
while budget >= 0:
    cmd = input()
    if cmd == "ACTION":
        break

    try:
        cmd_to_float = float(cmd)
        budget = round(budget - cmd_to_float, 2)
    except:
        pass

    if not cmd.isdigit():
        if len(cmd) > 15:
            budget -= (budget * 0.2)

if budget > 0:
    print(f"We are left with {budget:.2f} leva.")
else:
    print(f"We need {-budget:.2f} leva for our actors.")

