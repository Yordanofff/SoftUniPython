n = int(input())
for i in range(1, n + 1):
    num_dashes = n - 2
    if i == 1 or i == n:
        symbol = "+"
    else:
        symbol = "|"
    if n == 2:
        print(f"{symbol} {symbol}")
    else:
        print(f"{symbol} {' '.join('-' * num_dashes)} {symbol}")
