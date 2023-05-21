import sys

n = int(input())

all_odd, all_even = [], []
min_odd = min_even = sys.maxsize
max_odd = max_even = -sys.maxsize

for i in range(1, n + 1):
    num = float(input())
    if i % 2 == 0:
        all_even.append(num)
        if num < min_even:
            min_even = num
        if num > max_even:
            max_even = num
    else:
        all_odd.append(num)
        if num < min_odd:
            min_odd = num
        if num > max_odd:
            max_odd = num

print(f"OddSum={sum(all_odd):.2f},")
if min_odd != sys.maxsize:
    print(f"OddMin={min_odd:.2f},")
else:
    print(f"OddMin=No,")
if max_odd != -sys.maxsize:
    print(f"OddMax={max_odd:.2f},")
else:
    print(f"OddMax=No,")

print(f"EvenSum={sum(all_even):.2f},")

if min_even != sys.maxsize:
    print(f"EvenMin={min_even:.2f},")
else:
    print(f"EvenMin=No,")
if max_even != -sys.maxsize:
    print(f"EvenMax={max_even:.2f}")
else:
    print(f"EvenMax=No")
