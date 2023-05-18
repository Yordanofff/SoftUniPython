capacity = int(input())
num_fans = int(input())

sectors = {"A": 0, "B": 0, "V": 0, "G": 0}

for i in range(num_fans):
    sector = input()
    sectors[sector] += 1

for i in sectors:
    print(f"{sectors[i] / num_fans * 100:.2f}%")

print(f"{num_fans / capacity * 100:.2f}%")
