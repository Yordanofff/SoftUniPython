skumriq_price_per_kg = float(input())
caca_price_per_kg = float(input())

palamud = float(input())
safrid = float(input())
midi = int(input())

palamud_price = 1.6 * skumriq_price_per_kg
safrid_price = 1.8 * caca_price_per_kg
midi_price = 7.5

total_price = palamud * palamud_price + safrid * safrid_price + midi * midi_price

print(f"{total_price:.2f}")