def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


a = int(input())
b = int(input())
c = int(input())

for i in range(1, a + 1):
    for j in range(2, b + 1):
        for k in range(1, c + 1):
            if i % 2 == 0 and k % 2 == 0 and is_simple(j):
                print(f"{i} {j} {k}")
