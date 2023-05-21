w = int(float(input()) * 100)  # cm
h = int(float(input()) * 100)  # cm

h -= 100  # path

desk_w = 120
desk_h = 70

num_desks_per_row = h // desk_h
num_desks_per_col = w // desk_w

total_desks = num_desks_per_row * num_desks_per_col - 3

print(total_desks)
