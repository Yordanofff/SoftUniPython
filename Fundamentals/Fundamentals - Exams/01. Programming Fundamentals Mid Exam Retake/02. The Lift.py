people = int(input())
lifts = [int(i) for i in input().split()]
available_seats = len(lifts) * 4 - sum(lifts)

is_no_people_left = False
people_that_will_need_to_wait = 0
full_fit = True if people == available_seats else False
if people >= available_seats:
    people_that_will_need_to_wait = people - available_seats
    lifts = [4 for i in range(len(lifts))]
else:
    for i, free_seats_in_lift in enumerate(lifts):
        for j in range(4 - free_seats_in_lift):
            people -= 1
            lifts[i] += 1
            if people == 0:
                is_no_people_left = True
                # all people have seats in the lift
                break
        if is_no_people_left:
            break

if not full_fit:
    if is_no_people_left:
        print("The lift has empty spots!")
    else:
        print(f"There isn't enough space! {people_that_will_need_to_wait} people in a queue!")

print(" ".join([str(i) for i in lifts]))
