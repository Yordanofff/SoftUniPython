n = int(input())
list_num = []
for _ in range(n):
    num = int(input())
    list_num.append(num)

avg = sum(list_num) / len(list_num)
print(f"{avg:.2f}")
