days = int(input()) - 1
room_type = input()
review = input()

prices = {"room for one person": 18, "apartment": 25, "president apartment": 35}

discount = 0
if room_type == "apartment":
    if days < 10:
        discount = 0.3
    elif days < 15:
        discount = 0.35
    else:
        discount = 0.5
elif room_type == "president apartment":
    if days < 10:
        discount = 0.1
    elif days < 15:
        discount = 0.15
    else:
        discount = 0.2

price_no_disc = days * prices[room_type]
price_with_disc = price_no_disc * (1-discount)

if review == "positive":
    final_price = price_with_disc * 1.25
else:
    final_price = price_with_disc * 0.9

print(f"{final_price:.2f}")
