budget = float(input())
season = input()

if budget <= 100:
    destination = "Bulgaria"
    money_to_spend = budget * 0.7  # winter
    if season == "summer":
        money_to_spend = budget * 0.3
elif budget <= 1000:
    destination = "Balkans"
    money_to_spend = budget * 0.8  # winter
    if season == "summer":
        money_to_spend = budget * 0.4
else:
    destination = "Europe"
    money_to_spend = budget * 0.9

type = "Camp" if season == "summer" and destination != "Europe" else "Hotel"

print(f"Somewhere in {destination}")
print(f"{type} - {money_to_spend:.2f}")