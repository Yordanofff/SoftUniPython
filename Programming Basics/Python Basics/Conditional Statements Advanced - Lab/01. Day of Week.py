def week_day(day_num):
    if day_num == 1:
        return "Monday"
    elif day_num == 2:
        return "Tuesday"
    elif day_num == 3:
        return "Wednesday"
    elif day_num == 4:
        return "Thursday"
    elif day_num == 5:
        return "Friday"
    elif day_num == 6:
        return "Saturday"
    elif day_num == 7:
        return "Sunday"
    else:
        return "Error"


day = int(input())

print(week_day(day))