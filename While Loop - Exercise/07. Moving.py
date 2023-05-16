a = int(input())
b = int(input())
c = int(input())

room_size_sqm = a * b * c

cmd = input()
total_box_size_sqm = 0
while cmd != "Done":
    total_box_size_sqm += int(cmd)
    if total_box_size_sqm > room_size_sqm:
        print(f"No more free space! You need {total_box_size_sqm - room_size_sqm} Cubic meters more.")
        break
    cmd = input()

if cmd == "Done":
    if total_box_size_sqm < room_size_sqm:
        print(f"{room_size_sqm - total_box_size_sqm} Cubic meters left.")
