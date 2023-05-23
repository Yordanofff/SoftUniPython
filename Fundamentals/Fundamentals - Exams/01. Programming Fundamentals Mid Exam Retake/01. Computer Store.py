component_prices = []
is_pc_build = False
while True:
    cmd = input()
    if cmd in ["special", "regular"]:
        is_pc_build = True
        break

    if float(cmd) < 0:
        print("Invalid price!")
    else:
        component_prices.append(float(cmd))

if sum(component_prices) == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {sum(component_prices):.2f}$")
    print(f"Taxes: {sum(component_prices) * 0.2:.2f}$")
    print(f"-----------")
    total_price = sum(component_prices) * 1.2
    if cmd == "special":
        total_price *= 0.9
    print(f"Total price: {total_price:.2f}$")
