n = int(input())
n += 1
for i in range(n):
    num_spaces = n - i
    mid_part = " | "
    if i == 0:
        print(f"{' ' * (num_spaces - 1)}{mid_part}")
    else:
        print(f"{' ' * (num_spaces - 1)}{'*' * i}{mid_part}{'*' * i}")
