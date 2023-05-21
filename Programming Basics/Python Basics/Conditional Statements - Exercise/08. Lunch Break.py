from math import ceil

series_name = input()
episode_length = int(input())
lunch_break_length = int(input())

time_to_eat = lunch_break_length/8
time_to_rest = lunch_break_length/4
remaining_time = lunch_break_length - time_to_eat - time_to_rest

if episode_length <= remaining_time:
    print(f"You have enough time to watch {series_name} and left with {ceil(remaining_time - episode_length)} minutes free time.")
else:
    print(f"You don't have enough time to watch {series_name}, you need {ceil(episode_length-remaining_time)} more minutes.")