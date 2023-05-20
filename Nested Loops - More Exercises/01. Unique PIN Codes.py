up_1 = int(input())
up_2 = int(input())
up_3 = int(input())


def is_simple(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(1, up_1 + 1):
    for j in range(1, up_2 + 1):
        for k in range(1, up_3 + 1):
            if i % 2 == 0 and k % 2 == 0 and is_simple(j):
                print(f"{i} {j} {k}")
