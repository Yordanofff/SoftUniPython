month = input()
days = int(input())

studio_prices = {"May": 50, "June": 75.20, "July": 76, "August": 76, "September": 75.20, "October": 50}
apart_prices = {"May": 65, "June": 68.70, "July": 77, "August": 77, "September": 68.70, "October": 65}

def get_discount(month, days, is_studio: bool):
    discount = 0
    if is_studio:
        if month in ["May", "October"]:
            if days > 14:
                discount = 0.3
            elif days > 7:
                discount = 0.05
        elif month in ["June", "September"] and days > 14:
            discount = 0.2
    else:
        if days > 14:
            discount = 0.1
    return discount

price_studio_no_disc = days * studio_prices[month]
price_studio_with_disc = price_studio_no_disc * (1-get_discount(month, days, True))

price_apart_no_disc = days * apart_prices[month]
price_apart_with_disc = price_apart_no_disc * (1-get_discount(month, days, False))

print(f"Apartment: {price_apart_with_disc:.2f} lv.")
print(f"Studio: {price_studio_with_disc:.2f} lv.")
