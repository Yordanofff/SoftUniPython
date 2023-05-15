destination = input()
money_required = float(input())
money_collected = 0

money_saved = float(input())
while money_collected >= money_required:
    money_collected += money_saved
    money_saved = float(input())

