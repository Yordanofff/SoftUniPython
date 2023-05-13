n = int(input())
if n == 2:
    print(" ".join("+" * 2))  # todo - doesn't work no matter what I try...
else:
    for i in range(1, n + 1):
        num_dashes = n - 2
        if i == 1 or i == n:
            symbol = "+"
        else:
            symbol = "|"
        print(f"{symbol} {' '.join('-' * num_dashes)} {symbol}")
