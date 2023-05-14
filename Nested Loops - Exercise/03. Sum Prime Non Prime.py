def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


cmd = input()

sum_prime = 0
sum_non_prime = 0
while cmd != "stop":
    if int(cmd) < 0:
        print("Number is negative.")
    else:
        if is_prime(int(cmd)):
            sum_prime += int(cmd)
        else:
            sum_non_prime += int(cmd)
    cmd = input()

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")
