year_tax = int(input())

shoes = 0.6 * year_tax
clothes = 0.8 * shoes
ball = 0.25 * clothes
accessories = 0.2 * ball

total = year_tax + shoes + clothes + ball + accessories
print(float(total))