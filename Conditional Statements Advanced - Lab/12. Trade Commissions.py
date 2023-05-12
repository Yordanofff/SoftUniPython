city = input()
sales = float(input())

sofia = [5, 7, 8, 12]
varna = [4.5, 7.5, 10, 13]
plovdiv = [5.5, 8, 12, 14.5]

if 0 <= sales <= 500:
   index = 0
elif 500 < sales <= 1000:
    index = 1
elif 1000 < sales <= 10000:
    index = 2
elif sales > 10000:
    index = 3
else:
    print("error")
    exit(1)

if city == "Sofia":
    sum = sofia[index]/100 * sales
elif city == "Varna":
    sum = varna[index]/100 * sales
elif city == "Plovdiv":
    sum = plovdiv[index]/100 * sales
else:
    print("error")
    exit(1)

print(f"{sum:.2f}")