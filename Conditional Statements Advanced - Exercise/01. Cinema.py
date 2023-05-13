type = input()
num_rows = int(input())
num_cols = int(input())

income = 0
capacity = num_rows * num_cols

if type == "Premiere":
    income = capacity * 12
elif type == "Normal":
    income = capacity * 7.5
elif type == "Discount":
    income = capacity * 5

print(f"{income:.2f} leva")