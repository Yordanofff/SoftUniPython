n = int(input())

diff = 0
sum_value = 0
for i in range(n):
    num_1 = int(input())
    num_2 = int(input())
    current_sum = num_1 + num_2
    if i == 0:
        sum_value = current_sum
    else:
        current_diff = abs(sum_value - current_sum)
        if diff < current_diff:
            diff = current_diff
        sum_value = current_sum

if diff > 0:
    print(f"No, maxdiff={diff}")
else:
    print(f"Yes, value={sum_value}")
