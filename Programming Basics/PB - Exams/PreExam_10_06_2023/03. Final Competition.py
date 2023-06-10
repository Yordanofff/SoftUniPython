expenses_bulgaria_perc = {"summer": 5, "winter": 8}
expenses_abroad_perc = {"summer": 10, "winter": 15}

num_dancers = int(input())
scores = float(input())
season = input()  # "summer" или "winter"
location = input()  # "Bulgaria" или "Abroad"

money_made = num_dancers * scores
expenses = money_made * expenses_bulgaria_perc[season] / 100

if location == "Abroad":
    money_made *= 1.5
    expenses = money_made * expenses_abroad_perc[season] / 100

money_total = money_made - expenses

money_for_charity = money_total * 0.75
money_for_dancers = money_total - money_for_charity  # or * 0.25

money_per_dancer = money_for_dancers / num_dancers

print(f"Charity - {money_for_charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")
