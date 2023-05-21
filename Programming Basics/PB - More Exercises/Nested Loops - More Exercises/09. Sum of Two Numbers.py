start = int(input())
end = int(input())
magic_number = int(input())

is_found = False
counter = 0
for i in range(start, end + 1):
    for j in range(start, end + 1):
        counter += 1
        if i + j == magic_number:
            print(f"Combination N:{counter} ({i} + {j} = {magic_number})")
            is_found = True
            break
    if is_found:
        break

if not is_found:
    print(f"{counter} combinations - neither equals {magic_number}")
