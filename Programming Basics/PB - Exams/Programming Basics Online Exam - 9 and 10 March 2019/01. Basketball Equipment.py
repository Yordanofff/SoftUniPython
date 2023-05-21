year_pay = int(input())

shoes = 0.6 * year_pay
clothes = 0.8 * shoes
ball = 0.25 * clothes
accessories = 0.2 * ball

total = year_pay + shoes + clothes + ball + accessories

print(f"{total:.2f}")
