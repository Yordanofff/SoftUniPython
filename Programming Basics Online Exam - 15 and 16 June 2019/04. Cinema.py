seats = int(input())
sum_people = 0
sum_money = 0
full = False

while True:

    word = input()
    if word == "Movie time!":
        break
    else:
        if sum_people >= seats or sum_people + int(word) > seats:
            print("The cinema is full.")
            full = True
            break
        word = int(word)
        if sum_people + word <= seats:
            sum_people += word

            if word % 3 == 0:
                sum_money -= 5

        else:
            break

if seats >= sum_people and not full:
    print(f"There are {seats - sum_people} seats left in the cinema.")

sum_money = sum_money + sum_people * 5
print(f"Cinema income - {sum_money} lv.")