products = int(input())

sold_cash = []
sold_card = []
is_cash = 0  # or card if %2 == 1
cmd = input()
while cmd != "End":
    if is_cash % 2 == 0:
        if int(cmd) > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sold_cash.append(int(cmd))
    else:
        if int(cmd) < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            sold_card.append(int(cmd))
    if sum(sold_cash) + sum(sold_card) >= products:
        break
    is_cash += 1
    cmd = input()

if cmd == "End":
    print("Failed to collect required money for charity.")
else:
    avg_cash = sum(sold_cash) / len(sold_cash)
    avg_card = sum(sold_card) / len(sold_card)

    print(f"Average CS: {avg_cash:.2f}")
    print(f"Average CC: {avg_card:.2f}")
