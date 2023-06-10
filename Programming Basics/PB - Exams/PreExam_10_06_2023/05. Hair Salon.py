haircut = {"mens": 15, "ladies": 20, "kids": 10}
color = {"touch up": 20, "full color": 30}

target = int(input())
cmd = input()
money_made = 0
target_reached = False
while cmd != "closed":
    if cmd == "haircut":
        money_made += haircut[input()]
    else:
        money_made += color[input()]
    if money_made >= target:
        target_reached = True
        break
    cmd = input()

if target_reached:
    print("You have reached your target for the day!")
else:
    print(f"Target not reached! You need {target - money_made}lv. more.")

print(f"Earned money: {money_made}lv.")
