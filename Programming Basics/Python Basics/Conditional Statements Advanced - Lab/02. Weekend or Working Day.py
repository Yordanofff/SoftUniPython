working_days = ["Monday","Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]

day = input()
if day in working_days:
    print("Working day")
elif day in weekends:
    print("Weekend")
else:
    print("Error")
    