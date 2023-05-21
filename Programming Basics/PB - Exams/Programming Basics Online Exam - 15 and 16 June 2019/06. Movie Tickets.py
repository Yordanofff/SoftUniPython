a1 = int(input())
a2 = int(input())
n = int(input())
list_letters = [chr(i) for i in range(a1, a2)]
s2 = [i for i in range(1, n)]
s3 = [i for i in range(1, int(n/2))]
for i in list_letters:
    s4 = ord(i)
    for j in s2:
        for n in s3:
            if s4 % 2 == 1 and (j+n+s4) % 2 == 1:
                print(f"{i}-{j}{n}{s4}")