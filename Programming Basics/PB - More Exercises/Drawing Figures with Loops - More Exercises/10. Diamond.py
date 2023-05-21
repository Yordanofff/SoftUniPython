n = int(input())

num_stars_top = 2 if n % 2 == 0 else 1

for i in range(1, int((n + 1) / 2) + 1):
    dashes_sides = int((n - num_stars_top) / 2 + 1 - i)
    dashes_mid = n - 2 - 2 * dashes_sides
    if i == 1:
        print(f"{'-' * dashes_sides}{'*' * num_stars_top}{'-' * dashes_sides}")
    else:
        print(f"{'-' * dashes_sides}*{'-' * dashes_mid}*{'-' * dashes_sides}")

for i in range(int((n + 1) / 2) - 1, 0, -1):
    dashes_sides = int((n - num_stars_top) / 2 + 1 - i)
    dashes_mid = n - 2 - 2 * dashes_sides
    if i == 1:
        print(f"{'-' * dashes_sides}{'*' * num_stars_top}{'-' * dashes_sides}")
    else:
        print(f"{'-' * dashes_sides}*{'-' * dashes_mid}*{'-' * dashes_sides}")
