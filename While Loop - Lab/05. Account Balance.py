cmd = input()
total = 0
while cmd != "NoMoreMoney":
    if float(cmd) > 0:
        print(f"Increase: {float(cmd):.2f}")
        total += float(cmd)
    else:
        print("Invalid operation!")
        break
    cmd = input()
print(f"Total: {total:.2f}")
