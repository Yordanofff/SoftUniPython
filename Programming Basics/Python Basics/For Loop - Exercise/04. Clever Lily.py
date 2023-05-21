n = int(input())
washing_machine = float(input())
toy_price = int(input())

toys = 0
money = 0
times_brother_got_money = 0

for i in range(1, n + 1):
    if i % 2 == 1:
        toys += 1
    else:
        times_brother_got_money += 1
        money += 10 * times_brother_got_money

money = money - times_brother_got_money
toys_money = toy_price * toys
total_money = money + toys_money

if washing_machine <= total_money:
    print(f"Yes! {total_money - washing_machine:.2f}")
else:
    print(f"No! {washing_machine - total_money:.2f}")
