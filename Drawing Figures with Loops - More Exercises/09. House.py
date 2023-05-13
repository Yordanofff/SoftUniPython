n = int(input())

roof_rows = int((n + 1) / 2)
wall_sides_rows = n - roof_rows

for i in range(1, roof_rows + 1):
    top_stars = 2 if n % 2 == 0 else 1
    underscore_count_side = int((n - top_stars) / 2) + 1 - i
    print(f"{'-' * underscore_count_side}{'*' * (n - 2 * underscore_count_side)}{'-' * underscore_count_side}")

for i in range(wall_sides_rows):
    print(f"|{'*' * (n - 2)}|")
