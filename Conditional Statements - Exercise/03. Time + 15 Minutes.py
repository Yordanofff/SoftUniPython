h = int(input())
m = int(input())

new_m = m + 15
if new_m >= 60:
    h += 1
    new_m = new_m - 60

if h >= 24:
    h = h - 24

if new_m < 10:
    print(f"{h}:0{new_m}")
else:
    print(f"{h}:{new_m}")