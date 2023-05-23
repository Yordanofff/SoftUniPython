elements = [i for i in input().split()]

counter = 0
while True:
    cmd = input()
    if cmd == "end":
        print("Sorry you lose :(")
        print(" ".join(elements))
        break
    counter += 1
    a, b = cmd.split()
    a = int(a)
    b = int(b)

    if a == b or 0 > a or a > (len(elements) - 1) or 0 > b or b > (len(elements) - 1):
        print("Invalid input! Adding additional elements to the board")
        element_to_add = f"-{counter}a"
        mid = int(len(elements) / 2)
        elements = elements[0:mid] + [element_to_add, element_to_add] + elements[mid:]
    else:
        if elements[a] == elements[b]:

            print(f"Congrats! You have found matching elements - {elements[int(a)]}!")

            bigger = a
            smaller = b
            if b > a:
                bigger = b
                smaller = a

            elements.pop(bigger)
            elements.pop(smaller)

            if len(elements) == 0:
                print(f"You have won in {counter} turns!")
                break
        else:
            print("Try again!")
