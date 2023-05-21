num_months = int(input())

total_el = 0
for i in range(num_months):
    electricity = float(input())
    total_el += electricity

total_water = num_months * 20
total_inet = num_months * 15
total_other = (total_el + total_inet + total_water) * 1.2

total_all = total_other + total_other / 1.2

avg = total_all / num_months

print(f"Electricity: {total_el:.2f} lv")
print(f"Water: {total_water:.2f} lv")
print(f"Internet: {total_inet:.2f} lv")
print(f"Other: {total_other:.2f} lv")
print(f"Average: {avg:.2f} lv")
