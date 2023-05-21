name_1 = input()
name_2 = input()

score_1 = 0
score_2 = 0
end_of_game_entered = False
while True:
    card_1 = input()
    if card_1 == "End of game":
        end_of_game_entered = True
        break
    card_2 = input()

    card_1 = int(card_1)
    card_2 = int(card_2)

    if card_1 == card_2:
        print("Number wars!")

        card_1 = int(input())  # 2-9
        card_2 = int(input())  # 2-9

        # don't sum up the score when in number wars! (:
        if card_1 > card_2:
            print(f"{name_1} is winner with {score_1} points")
        else:
            print(f"{name_2} is winner with {score_2} points")
            
        break
    else:
        diff = abs(card_1 - card_2)
        if card_1 > card_2:
            score_1 += diff
        else:
            score_2 += diff

if end_of_game_entered:
    print(f"{name_1} has {score_1} points")
    print(f"{name_2} has {score_2} points")
