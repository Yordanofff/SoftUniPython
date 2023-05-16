money_lv = float(input())

money_lv_to_coins = int(money_lv * 100)

# all_coins_used = []
total_num_coins = 0
while money_lv_to_coins != 0:

    for i in [200, 100, 50, 20, 10, 5, 2, 1]:
        num_coins = money_lv_to_coins // i
        if num_coins > 0:
            # for _ in range(num_coins):
            #     all_coins_used.append(i)
            total_num_coins += num_coins

            money_lv_to_coins -= i * num_coins

print(total_num_coins)
