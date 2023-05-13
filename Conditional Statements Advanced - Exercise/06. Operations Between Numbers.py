num1 = int(input())
num2 = int(input())
operator = input()

if num2 == 0:
    print(f"Cannot divide {num1} by zero")
    exit(1)
result = eval(str(num1) + operator + str(num2))

odd_or_even = "odd"
if result % 2 == 0:
    odd_or_even = "even"

if operator == "/":
    print(f"{num1} {operator} {num2} = {result:.2f}")
elif operator == "%":
    print(f"{num1} {operator} {num2} = {result}")
else:
    print(f"{num1} {operator} {num2} = {result} - {odd_or_even}")

