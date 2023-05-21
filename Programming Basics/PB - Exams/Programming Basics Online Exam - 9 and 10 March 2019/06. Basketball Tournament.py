total_games = 0
won_games = 0
while True:
    tournament_name = input()
    if tournament_name == "End of tournaments":
        break
    num_games = int(input())

    for game in range(1, num_games + 1):
        team_1 = int(input())
        team_2 = int(input())
        diff = abs(team_1 - team_2)
        if team_1 > team_2:
            result = "win"
            won_games += 1
        else:
            result = "lost"
        total_games += 1
        print(f"Game {game} of tournament {tournament_name}: {result} with {diff} points.")

print(f"{won_games / total_games * 100:.2f}% matches win")
print(f"{(total_games - won_games) / total_games * 100:.2f}% matches lost")
