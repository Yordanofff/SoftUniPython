GREEN_COVERAGE_PER_LITER = 3.4
RED_COVERAGE_PER_LITER = 4.3

x = float(input())
y = float(input())
h = float(input())

walls_sqm = (x + y) * 2 * x
doors_and_windows = 1.2 * 2 + 2 * (1.5 ** 2)
green_area = walls_sqm - doors_and_windows

green_paint_needed = green_area / GREEN_COVERAGE_PER_LITER

roof_sides = 2 * x * y
roof_triangles = x * h
roof_area = roof_sides + roof_triangles

red_paint_needed = roof_area / RED_COVERAGE_PER_LITER

print(f"{green_paint_needed:.2f}")
print(f"{red_paint_needed:.2f}")
