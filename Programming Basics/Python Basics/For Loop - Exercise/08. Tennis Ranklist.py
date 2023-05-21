from math import floor

scores = {"W": 2000, "F": 1200, "SF": 720}

num_tournaments = int(input())
starting_points = int(input())

points_from_tournaments = 0
num_wins = 0
for i in range(num_tournaments):
    position_in_tournament = input()
    if position_in_tournament == "W":
        num_wins += 1
    points = scores[position_in_tournament]
    points_from_tournaments += points

total_scores = starting_points + points_from_tournaments
avg_points_per_tournament = floor(points_from_tournaments / num_tournaments)
percentage_won = num_wins / num_tournaments * 100

print(f"Final points: {total_scores}")
print(f"Average points: {avg_points_per_tournament}")
print(f"{percentage_won:.2f}%")
