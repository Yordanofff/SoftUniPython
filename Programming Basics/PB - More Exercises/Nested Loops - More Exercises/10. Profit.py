lv_1 = int(input())
lv_2 = int(input())
lv_5 = int(input())
lv_sum = int(input())

for i in range(lv_1+1):
    for j in range(lv_2+1):
        for k in range(lv_5+1):
            if i*1 + j*2 + k*5 == lv_sum:
                print(f"{i} * 1 lv. + {j} * 2 lv. + {k} * 5 lv. = {lv_sum} lv.")
