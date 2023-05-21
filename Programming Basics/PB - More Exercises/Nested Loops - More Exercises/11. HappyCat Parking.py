num_days = int(input())
num_hours_per_day = int(input())
total = 0
for day in range(1, num_days + 1):
    price_per_day = 0
    for hour in range(1, num_hours_per_day + 1):
        if day % 2 == 0 and hour % 2 != 0:
            price_per_hour = 2.5
        elif day % 2 != 0 and hour % 2 == 0:
            price_per_hour = 1.25
        else:
            price_per_hour = 1
        price_per_day += price_per_hour
    print(f"Day: {day} - {price_per_day:.2f} leva")
    total += price_per_day

print(f"Total: {total:.2f} leva")
