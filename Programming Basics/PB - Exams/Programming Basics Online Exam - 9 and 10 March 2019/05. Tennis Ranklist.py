from math import floor

num_tournaments = int(input())
starting_points = int(input())

won = 0
points_from_tournaments = 0
for _ in range(num_tournaments):
    result = input()
    if result == "W":
        points_from_tournaments += 2000
        won += 1
    elif result == "F":
        points_from_tournaments += 1200
    elif result == "SF":
        points_from_tournaments += 720

final_points = starting_points + points_from_tournaments
avg_per_tournament = points_from_tournaments / num_tournaments
percent_won = won / num_tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {floor(avg_per_tournament)}")
print(f"{percent_won:.2f}%")
