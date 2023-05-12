price_pen = 5.8
price_markers = 7.2
cleaner = 1.20

num_pens = int(input())
num_markers = int(input())
num_cleaners = int(input())
discount = int(input())/100

price = num_pens * price_pen + num_markers * price_markers + num_cleaners * cleaner
price_with_discount = price - price * discount
print(price_with_discount)