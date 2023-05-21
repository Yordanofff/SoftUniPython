

name = input()

is_failed = False
failed = 0
successful = 0
remaining_points = 301
while True:
    sdt = input()
    if sdt == "Retire":
        is_failed = True
        break
    points = int(input())

    if sdt == "Double":
        points *= 2
    elif sdt == "Triple":
        points *= 3

    if points <= remaining_points:
        remaining_points -= points
        successful += 1
    else:
        failed += 1

    if remaining_points == 0:
        print(f"{name} won the leg with {successful} shots.")
        break

if is_failed:
    print(f"{name} retired after {failed} unsuccessful shots.")