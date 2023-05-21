import string

alphabet = list(string.ascii_lowercase)

n = int(input())
l = int(input())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in alphabet[:l]:
            for d in alphabet[:l]:
                for e in range(1, n + 1):
                    if e > a and e > b:
                        print(f"{a}{b}{c}{d}{e}", end=' ')
