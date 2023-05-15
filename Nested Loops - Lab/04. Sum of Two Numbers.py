start = int(input())
end = int(input())
number_to_find = int(input())

count = 0
is_found = False
for i in range(start, end + 1):
    for j in range(start, end + 1):
        count += 1
        if i + j == number_to_find:
            is_found = True
            break
    if is_found:
        break

if is_found:
    print(f"Combination N:{count} ({i} + {j} = {number_to_find})")
else:
    print(f"{count} combinations - neither equals {number_to_find}")
