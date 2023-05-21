import sys

n = input()

min_n = sys.maxsize
while n != "Stop":
    if int(n) < min_n:
        min_n = int(n)
    n = input()
print(min_n)