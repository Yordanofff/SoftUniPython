n = int(input())
for i in range(1, n+1):
    list_digits_of_i = [int(j) for j in str(i)]
    sum_of_digits = sum(list_digits_of_i)
    if sum_of_digits in [5, 7, 11]:
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")