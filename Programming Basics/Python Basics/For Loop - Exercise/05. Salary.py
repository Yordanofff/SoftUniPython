fines = {"Facebook": 150, "Instagram": 100, "Reddit": 50}

num_tabs = int(input())
salary = int(input())

for i in range(num_tabs):
    site = input()
    if site in fines:
        salary -= fines[site]

if salary <= 0:
    print("You have lost your salary.")
else:
    print(salary)
