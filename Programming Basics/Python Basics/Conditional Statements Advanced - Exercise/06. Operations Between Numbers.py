def print_operations_between_nums(num1, num2, operator):
    if num2 == 0:
        print(f"Cannot divide {num1} by zero")
        return

    result = eval(str(num1) + operator + str(num2))

    odd_or_even = "even" if result % 2 == 0 else "odd"

    if operator == "/":
        print(f"{num1} {operator} {num2} = {result:.2f}")
    elif operator == "%":
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")


n1 = int(input())
n2 = int(input())
op = input()

print_operations_between_nums(n1, n2, op)
