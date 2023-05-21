def is_simple(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


from_a = int(input())
from_b = int(input())
to_a = int(input()) + from_a
to_b = int(input()) + from_b

for a in range(from_a, to_a + 1):
    for b in range(from_b, to_b + 1):
        if is_simple(a) and is_simple(b):
            print(f"{a}{b}")
