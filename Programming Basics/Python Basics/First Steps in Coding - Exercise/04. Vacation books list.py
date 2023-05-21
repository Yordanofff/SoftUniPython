num_pages = int(input())
num_pages_per_hour = int(input())
days = int(input())

hours_per_day = (num_pages/num_pages_per_hour)/days
print(int(hours_per_day))