def get_shop_msg(fruit, week_day, quantity):
    weekday_prices = {"banana": 2.50, "apple": 1.20, "orange": 0.85, "grapefruit": 1.45, "kiwi": 2.70,
                      "pineapple": 5.50,
                      "grapes": 3.85}

    weekend_prices = {"banana": 2.70, "apple": 1.25, "orange": 0.90, "grapefruit": 1.60, "kiwi": 3.00,
                      "pineapple": 5.60,
                      "grapes": 4.20}

    working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    weekend_days = ["Saturday", "Sunday"]

    if fruit not in weekday_prices:
        return "error"

    if week_day in weekend_days:
        return f"{quantity * weekend_prices[fruit]:.2f}"
    elif week_day in working_days:
        return f"{quantity * weekday_prices[fruit]:.2f}"
    return "error"

fruit = input()
week_day = input()
quantity = float(input())

print(get_shop_msg(fruit, week_day, quantity))