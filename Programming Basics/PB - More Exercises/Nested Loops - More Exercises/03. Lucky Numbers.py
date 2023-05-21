n = int(input())

for i in range(1000, 10000):
    first_two = str(i)[:2]
    last_two = str(i)[2:]
    str_i = str(i)
    a = int(str_i[0])
    b = int(str_i[1])
    c = int(str_i[2])
    d = int(str_i[3])
    if a + b == c + d and n % (a + b) == 0 and a != 0 and b != 0 and c != 0 and d != 0:
        print(i, end=' ')
