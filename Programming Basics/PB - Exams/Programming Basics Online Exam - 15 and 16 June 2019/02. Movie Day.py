available_time = int(input())
scene_count = int(input())
scene_time_required = int(input())

preparation_for_scene = 0.15 * available_time
shooting_time = scene_count * scene_time_required
total = int(shooting_time + preparation_for_scene)

if available_time > total:
    print(f"You managed to finish the movie on time! You have {available_time - total} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {total - available_time} minutes.")