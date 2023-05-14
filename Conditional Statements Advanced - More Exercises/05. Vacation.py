def vacation(budget: float, season: str):
    room_type = "Hotel"
    location = "Alaska"
    part_of_budget = 0.9
    if season == "Winter":
        location = "Morocco"

    if budget <= 1000:
        room_type = "Camp"
        location = "Alaska"
        part_of_budget = 0.65
        if season == "Winter":
            location = "Morocco"
            part_of_budget = 0.45
    elif budget <= 3000:
        room_type = "Hut"
        location = "Alaska"
        part_of_budget = 0.8
        if season == "Winter":
            location = "Morocco"
            part_of_budget = 0.6
    price = budget * part_of_budget
    print(f"{location} - {room_type} - {price:.2f}")


budget = float(input())
season = input()

vacation(budget, season)
