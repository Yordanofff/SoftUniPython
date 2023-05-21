a = int(input())
b = int(input())
num_pieces_total = a * b

pieces_eaten = 0
cmd = input()
while cmd != "STOP":
    pieces_eaten += int(cmd)
    if pieces_eaten >= num_pieces_total:
        print(f"No more cake left! You need {pieces_eaten - num_pieces_total} pieces more.")
        break
    cmd = input()

if cmd == "STOP":
    print(f"{num_pieces_total - pieces_eaten} pieces are left.")
