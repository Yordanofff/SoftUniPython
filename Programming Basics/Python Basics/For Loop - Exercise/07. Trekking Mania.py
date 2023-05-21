n = int(input())

g1 = g2 = g3 = g4 = g5 = 0
for _ in range(n):
    group = int(input())
    if group <= 5:
        g1 += group
    elif group <= 12:
        g2 += group
    elif group <= 25:
        g3 += group
    elif group <= 40:
        g4 += group
    else:
        g5 += group

sum_all = g1 + g2 + g3 + g4 + g5

print(f"{g1 / sum_all * 100:.2f}%")
print(f"{g2 / sum_all * 100:.2f}%")
print(f"{g3 / sum_all * 100:.2f}%")
print(f"{g4 / sum_all * 100:.2f}%")
print(f"{g5 / sum_all * 100:.2f}%")
