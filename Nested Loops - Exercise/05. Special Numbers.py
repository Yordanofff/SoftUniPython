def is_dividable_by_all(num: int, num_to_split: int):
    num_to_split_str = set(str(num_to_split))
    for i in num_to_split_str:
        if int(i) == 0 or num % int(i) != 0:
            return False
    return True


def is_special(num):
    for i in range(1111, 10000):
        if is_dividable_by_all(num, i):
            print(i, end=" ")


n = int(input())

is_special(n)
