a = int(input())
b = int(input())
max_pw = int(input())

a_starting = 35
b_starting = 64

list_chr = []
for i in range(a * b):
    ch_for_a = i + a_starting
    ch_for_b = i + b_starting

    if ch_for_a == 55:
        a_starting -= 21
    if ch_for_b == 96:
        b_starting -= 33

    a_ = chr(ch_for_a)
    b_ = chr(ch_for_b)

    list_chr.append(f"{a_}{b_}")  # #@
    list_chr.append(f"{b_}{a_}")  # @#


is_completed = False
counter = 0
for x in range(1, a + 1):
    for y in range(1, b + 1):
        if counter == max_pw:
            is_completed = True
            break
        print(f"{list_chr[counter * 2]}{x}{y}{list_chr[counter * 2 + 1]}", end='|')
        counter += 1
    if is_completed:
        break
