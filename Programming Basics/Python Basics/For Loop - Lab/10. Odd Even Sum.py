n = int(input())

odd = 0
even = 0

for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 1:
        odd += num
    else:
        even += num

if odd == even:
    print("Yes")
    print(f"Sum = {odd}")
else:
    print("No")
    print(f"Diff = {abs(odd - even)}")
