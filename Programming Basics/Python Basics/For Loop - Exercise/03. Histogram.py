n = int(input())

p_1 = p_2 = p_3 = p_4 = p_5 = 0

for i in range(n):
    num = int(input())
    if num < 200:
        p_1 += 1
    elif num < 400:
        p_2 += 1
    elif num < 600:
        p_3 += 1
    elif num < 800:
        p_4 += 1
    else:
        p_5 += 1

total = p_1 + p_2 + p_3 + p_4 + p_5

print(f"{p_1 / total * 100:.2f}%")
print(f"{p_2 / total * 100:.2f}%")
print(f"{p_3 / total * 100:.2f}%")
print(f"{p_4 / total * 100:.2f}%")
print(f"{p_5 / total * 100:.2f}%")
