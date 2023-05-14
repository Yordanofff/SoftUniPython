num_1 = int(input())
num_2 = int(input())

for i in range(num_1, num_2 + 1):
    sum_even = 0
    sum_odd = 0
    for j in range(6):
        if j % 2 == 0:
            sum_even += int(str(i)[j])
        else:
            sum_odd += int(str(i)[j])
    if sum_even == sum_odd:
        print(i, end=' ')
