n = int(input())

sum_1 = 0
sum_2 = 0

for i in range(n):
    num = int(input())
    sum_1 += num

for i in range(n):
    num = int(input())
    sum_2 += num

if sum_1 == sum_2:
    print(f" Yes, sum = {sum_1}")
else:
    print(f"No, diff = {abs(sum_1 - sum_2)}")
