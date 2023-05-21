budget = int(input())
cmd = input()

while not cmd == "End":
    budget -= int(cmd)
    if budget < 0:
        print("You went in overdraft!")
        break
    cmd = input()

if cmd == "End":
    print("You bought everything needed.")