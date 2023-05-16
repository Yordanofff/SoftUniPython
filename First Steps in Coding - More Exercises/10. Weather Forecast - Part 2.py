temp = float(input())

temp_val = "unknown"
if temp < 5:
    pass
elif temp <= 11.9:
    temp_val = "Cold"
elif temp <= 14.9:
    temp_val = "Cool"
elif temp <= 20:
    temp_val = "Mild"
elif temp <= 25.9:
    temp_val = "Warm"
elif temp <= 35:
    temp_val = "Hot"

print(temp_val)
