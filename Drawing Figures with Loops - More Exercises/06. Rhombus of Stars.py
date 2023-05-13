n = int(input())

for i in range(1, n + 1):
    num_spaces = n - i
    print(f"{' ' * num_spaces}{' '.join('*' * i)}")

for i in range(n - 1, 0, -1):
    num_spaces = n - i
    print(f"{' ' * num_spaces}{' '.join('*' * i)}")
