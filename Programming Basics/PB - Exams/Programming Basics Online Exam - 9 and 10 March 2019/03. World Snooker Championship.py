# Standard = {"Quarter final": 55.5, "Semi final": 75.88, "Final": 110.1}
# Premium = {"Quarter final": 105.2, "Semi final": 125.22, "Final": 160.66}
# VIP = {"Quarter final": 118.90, "Semi final": 300.4, "Final": 400}

dict_prices = {
    "Standard": {"Quarter final": 55.5, "Semi final": 75.88, "Final": 110.1},
    "Premium": {"Quarter final": 105.2, "Semi final": 125.22, "Final": 160.66},
    "VIP": {"Quarter final": 118.90, "Semi final": 300.4, "Final": 400}
}

pic_price = 40

event_type = input()  # “Quarter final ”, “Semi final” или “Final“
ticket_type = input()
num_tickets = int(input())
picture = input()

is_picture = True if picture == "Y" else False

price = dict_prices[ticket_type][event_type] * num_tickets

if price > 4000:
    pic_price = 0
    price = price * 0.75
elif price > 2500:
    price = price * 0.9

if is_picture:
    price += pic_price * num_tickets

print(f"{price:.2f}")
