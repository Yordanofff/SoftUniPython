deposited_money = float(input())
num_months = int(input())
interest = float(input())

win = deposited_money + num_months * ((deposited_money * interest/100)/12)
print(win)