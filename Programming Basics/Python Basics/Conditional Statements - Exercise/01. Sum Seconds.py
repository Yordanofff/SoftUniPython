t1 = int(input())
t2 = int(input())
t3 = int(input())

t_total = t1 + t2 + t3
min = t_total / 60
sec = t_total % 60
if sec < 10:
    print(f"{int(min)}:0{sec}")
else:
    print(f"{int(min)}:{sec}")