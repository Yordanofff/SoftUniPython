hour = int(input())
day_name = input()

working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

if day_name in working_days and 10 <= hour <= 18:
    print("open")
else:
    print("closed")