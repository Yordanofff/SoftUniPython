rounds = int(input())

all_nums = []

# loop calculating the scores
total_score = 0
for i in range(rounds):
    points = int(input())
    all_nums.append(points)
    if 0 <= points <= 9:
        total_score += points * 0.2
    elif 10 <= points <= 19:
        total_score += points * 0.3
    elif 20 <= points <= 29:
        total_score += points * 0.4
    elif 30 <= points <= 39:
        total_score += 50
    elif 40 <= points <= 50:
        total_score += 100
    else:
        total_score /= 2

# calculating %
r1 = len([i for i in all_nums if 0 <= i <= 9]) / len(all_nums) * 100
r2 = len([i for i in all_nums if 10 <= i <= 19]) / len(all_nums) * 100
r3 = len([i for i in all_nums if 20 <= i <= 29]) / len(all_nums) * 100
r4 = len([i for i in all_nums if 30 <= i <= 39]) / len(all_nums) * 100
r5 = len([i for i in all_nums if 40 <= i <= 50]) / len(all_nums) * 100
r6 = len([i for i in all_nums if 50 < i or i < 0]) / len(all_nums) * 100

print(f"{total_score:.2f}")
print(f"From 0 to 9: {r1:.2f}%")
print(f"From 10 to 19: {r2:.2f}%")
print(f"From 20 to 29: {r3:.2f}%")
print(f"From 30 to 39: {r4:.2f}%")
print(f"From 40 to 50: {r5:.2f}%")
print(f"Invalid numbers: {r6:.2f}%")
