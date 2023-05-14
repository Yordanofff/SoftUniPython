def bike(num_jun, num_sen, trace):
    juniors = {"trail": 5.50, "cross-country": 8, "downhill": 12.25, "road": 20}
    seniors = {"trail": 7, "cross-country": 9.5, "downhill": 13.75, "road": 21.50}

    total_num = num_sen + num_jun

    discount = 0
    if total_num >= 50 and trace == "cross-country":
        discount = 0.25

    money = num_jun * juniors[trace] + num_sen * seniors[trace]
    money_with_discount = money * (1 - discount)

    money_spend = 0.05 * money_with_discount

    money_left = money_with_discount - money_spend

    print(f"{money_left:.2f}")


num_juniors = int(input())
num_seniors = int(input())
trace_type = input()

bike(num_juniors, num_seniors, trace_type)
