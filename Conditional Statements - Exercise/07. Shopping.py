budget = float(input())
num_gpu = int(input())
num_cpu = int(input())
num_ram = int(input())

gpu_price = 250 * num_gpu
cpu_price = 0.35 * gpu_price * num_cpu
ram_price = 0.1 * gpu_price * num_ram
total = gpu_price + cpu_price + ram_price

if num_gpu > num_cpu:
    total = total * 0.85
if budget >= total:
    print(f"You have {(budget-total):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total-budget):.2f} leva more!")