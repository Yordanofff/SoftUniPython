import sys

n = input()

max_n = -sys.maxsize
while n != "Stop":
    if int(n) > max_n:
        max_n = int(n)
    n = input()
print(max_n)