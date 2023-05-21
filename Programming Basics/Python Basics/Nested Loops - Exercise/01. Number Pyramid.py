n = int(input())

current_num = 0
for row in range(1, n + 1):
    for _ in range(1, row + 1):
        col = current_num + 1
        print(col, end=' ')
        current_num = col
        if current_num == n:
            break
    if current_num == n:
        break
    print()
