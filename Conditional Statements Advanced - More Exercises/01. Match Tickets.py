t1 = 499.99
t2 = 249.99

budget = float(input())
category = input()  # VIP/normal
num_people = int(input())

if 1 <= num_people <= 4:
    percent_of_budget_for_transport = 0.75
elif num_people <= 9:
    percent_of_budget_for_transport = 0.6
elif num_people <= 24:
    percent_of_budget_for_transport = 0.5
elif num_people <= 49:
    percent_of_budget_for_transport = 0.4
else:
    percent_of_budget_for_transport = 0.25

transport_cost = budget * percent_of_budget_for_transport

tickets = t2 * num_people
if category == "VIP":
    tickets = t1 * num_people

total_spend = tickets + transport_cost
if budget > total_spend:
    print(f"Yes! You have {budget - total_spend:.2f} leva left.")
else:
    print(f"Not enough money! You need {total_spend - budget:.2f} leva.")
