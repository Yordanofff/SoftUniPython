n = int(input())

mid_times = int((n + 1) / 2)

for i in range(1, n + 1):
    mid_part = " "
    if i == 1 or i == n:
        print(f"{'*' * (n * 2)}{' ' * n}{'*' * (n * 2)}")
    else:
        if i == mid_times:
            mid_part = "|"
        print(f"*{'/' * (n * 2 - 2)}*{mid_part * n}*{'/' * (n * 2 - 2)}*")
