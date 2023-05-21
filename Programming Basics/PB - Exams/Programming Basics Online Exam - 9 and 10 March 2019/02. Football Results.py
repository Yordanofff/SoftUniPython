a = input()
b = input()
c = input()

num_win = 0
num_lose = 0
num_drawn = 0
for i in a, b, c:
    x = i.split(":")[0]
    y = i.split(":")[1]
    if x > y:
        num_win += 1
    elif x < y:
        num_lose += 1
    else:
        num_drawn += 1

print(f"Team won {num_win} games.")
print(f"Team lost {num_lose} games.")
print(f"Drawn games: {num_drawn}")
