num_floors = int(input())
num_rooms_per_floor = int(input())

for floor_num in range(num_floors, 0, -1):
    if floor_num == num_floors:
        for room in range(num_rooms_per_floor):
            print(f"L{floor_num}{room}", end=" ")
        print()
    else:
        if floor_num % 2 == 1:
            for room in range(num_rooms_per_floor):
                print(f"A{floor_num}{room}", end=" ")
            if floor_num != 0:
                print()
        else:
            for room in range(num_rooms_per_floor):
                print(f"O{floor_num}{room}", end=" ")
            print()
