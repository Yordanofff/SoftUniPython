def flowers_app(f_1, f_2, f_3, season, holiday):
    Spring_Summer = [2, 4.1, 2.5]
    Аutumn_Winter = [3.75, 4.5, 4.15]

    total_num_flowers = f_1 + f_2 + f_3
    is_holiday = True if holiday == "Y" else False
    prices_list = Spring_Summer if season in ["Spring", "Summer"] else Аutumn_Winter
    increase_percentage = 0.15 if is_holiday else 0

    spend_1 = f_1 * prices_list[0]
    spend_2 = f_2 * prices_list[1]
    spend_3 = f_3 * prices_list[2]
    total_spend = (spend_1 + spend_2 + spend_3) * (1 + increase_percentage)

    discount = 0
    if f_3 > 7 and season == "Spring":
        discount = 0.05
    if f_2 >= 10 and season == "Winter":
        discount = 0.1

    total_spend_with_discount = total_spend * (1 - discount)

    discount = 0
    if total_num_flowers > 20:
        discount = 0.2

    total_spend_with_discount = total_spend_with_discount * (1 - discount) + 2
    print(f"{total_spend_with_discount:.2f}")


f_1 = int(input())
f_2 = int(input())
f_3 = int(input())
season = input()
holiday = input()

flowers_app(f_1, f_2, f_3, season, holiday)
