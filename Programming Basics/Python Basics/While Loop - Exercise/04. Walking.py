goal = 10_000
total_steps = 0
is_goal_reached = False

while total_steps <= goal:

    steps = input()

    if steps == "Going home":
        steps_to_get_home = int(input())
        total_steps += steps_to_get_home
        if total_steps < goal:
            print(f"{goal - total_steps} more steps to reach goal.")
            break
        else:
            is_goal_reached = True
    else:
        total_steps += int(steps)
        if total_steps >= goal:
            is_goal_reached = True

if is_goal_reached:
    print("Goal reached! Good job!")
    if total_steps > goal:
        print(f"{total_steps - goal} steps over the goal!")
