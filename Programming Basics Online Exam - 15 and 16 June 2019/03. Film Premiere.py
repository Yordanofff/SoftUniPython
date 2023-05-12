name = input()
choice = input()
ticket_count = int(input())

if name == "John Wick":
    price = 12
    if choice == "Popcorn":
        price = 15
    elif choice == "Menu":
        price = 19
elif name == "Star Wars":
    price = 18
    if choice == "Popcorn":
        price = 25
    elif choice == "Menu":
        price = 30
elif name == "Jumanji":
    price = 9
    if choice == "Popcorn":
        price = 11
    elif choice == "Menu":
        price = 14


discount = 0

if name == "Star Wars" and ticket_count >= 4:
    discount = 0.30
elif name == "Jumanji" and ticket_count == 2:
    discount = 0.15

total_no_discount = price * ticket_count
total = total_no_discount - total_no_discount*discount
print(f"Your bill is {total:.2f} leva.")