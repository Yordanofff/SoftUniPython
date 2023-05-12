num = int(input())

if num < 100:
    bonus = 5
elif num <= 1000:
    bonus = num * 0.2
else:
    bonus = num * 0.1

extra_bonus = 0
if num % 2 == 0:
    extra_bonus = 1
elif num % 10 == 5:
    extra_bonus = 2

print(bonus + extra_bonus)
print(bonus + extra_bonus + num)