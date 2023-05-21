n = int(input())

all_nums = []

for i in range(n):
    num = int(input())
    all_nums.append(num)

if max(all_nums) == sum(all_nums) / 2:
    print("Yes")
    print(f"Sum = {max(all_nums)}")
else:
    print("No")
    print(f"Diff = {abs(max(all_nums) - (sum(all_nums) - max(all_nums)))}")
