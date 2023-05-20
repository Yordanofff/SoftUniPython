men = int(input()) +1
women = int(input()) + 1
tables = int(input())

all_possible_variants = []
counter = 0
is_no_space = False
for i in range(1, men):
    for j in range(1, women):
        print(f"({i} <-> {j})", end=' ')
        counter += 1
        if counter == tables:
            is_no_space = True
            break
    if is_no_space:
        break
