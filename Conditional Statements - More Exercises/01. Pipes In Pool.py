V = int(input())
P1 = int(input())  # per hour
P2 = int(input())  # per hour
H = float(input())  # hours

litters_filled = (P1 + P2) * H

if litters_filled > V:
    print(f"For {H:.2f} hours the pool overflows with {litters_filled - V:.2f} liters.")
else:
    pool_perc = litters_filled / V * 100
    P1_perc = P1 / litters_filled * H * 100
    P2_perc = P2 / litters_filled * H * 100
    print(f"The pool is {pool_perc:.2f}% full. Pipe 1: {P1_perc:.2f}%. Pipe 2: {P2_perc:.2f}%.")
