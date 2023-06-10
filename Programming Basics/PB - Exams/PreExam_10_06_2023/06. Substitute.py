def get_range(range_small, range_large):
    if range_small == range_large:
        return [range_small, ]
    step = 1
    if range_small > range_large:
        step = -1
    return [*range(range_small, range_large + step, step)]


K = int(input())
L = int(input())
M = int(input())
N = int(input())

possible_numbers = []
for i in get_range(K, 8):
    for j in get_range(9, L):
        if i % 2 == 0 and j % 2 == 1:
            possible_numbers.append(f"{i}{j}")

possible_numbers_2 = []
for i in get_range(M, 8):
    for j in get_range(9, N):
        if i % 2 == 0 and j % 2 == 1:
            possible_numbers_2.append(f"{i}{j}")

NUM_TO_PRINT = 6
numbers_printed = 0
num_limit_reached = False
for num in possible_numbers:
    for num2 in possible_numbers_2:
        if num == num2:
            print("Cannot change the same player.")
        else:
            numbers_printed += 1
            print(f"{num} - {num2}")
            if numbers_printed == NUM_TO_PRINT:
                num_limit_reached = True
                break
    if num_limit_reached:
        break
