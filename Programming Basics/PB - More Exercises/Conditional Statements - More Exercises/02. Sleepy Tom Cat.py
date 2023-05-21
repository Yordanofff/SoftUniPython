YEAR_DAYS = 365
PLAY_TIME_NEEDED = 30_000  # minutes

holidays = int(input())

working_days = YEAR_DAYS - holidays

play_time = holidays * 127 + working_days * 63

diff = abs(PLAY_TIME_NEEDED - play_time)

h = diff // 60
m = diff % 60

if play_time <= PLAY_TIME_NEEDED:
    print("Tom sleeps well")
    print(f"{h} hours and {m} minutes less for play")
else:
    print("Tom will run away")
    print(f"{h} hours and {m} minutes more for play")
