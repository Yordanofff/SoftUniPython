DAYS = 5
money_per_day = float(input())
money_per_day_from_sales = float(input())
total_money_spent = float(input())
money_needed = float(input())

total_money_made = (money_per_day + money_per_day_from_sales) * DAYS

total_money_made_after_spending = total_money_made - total_money_spent

if total_money_made_after_spending >= money_needed:
    print(f"Profit: {total_money_made_after_spending:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {money_needed - total_money_made_after_spending:.2f} BGN.")
