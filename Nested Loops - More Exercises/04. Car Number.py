start = int(input())
end = int(input()) + 1

for a in range(start, end):
    for b in range(start, end):
        for c in range(start, end):
            for d in range(start, end):
                if (a % 2 == 0 and d % 2 != 0) or (a % 2 != 0 and d % 2 == 0):
                    if a > d and ((b + c) % 2 == 0):
                        print(f"{a}{b}{c}{d}", end=' ')
